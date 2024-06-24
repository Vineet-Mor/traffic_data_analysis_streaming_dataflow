import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.pubsub import ReadFromPubSub

PROJECT_ID="quixotic-treat-419302"
class ParsePubSubMessage(beam.DoFn):
    def process(self, message):
        import json
        record = json.loads(message.decode('utf-8'))
        yield record

class CalculateAverageSpeed(beam.DoFn):
    def process(self, element, window=beam.DoFn.WindowParam):
        average_speed = sum(element['speed']) / len(element['speed'])
        yield {
            'timestamp': window.end.to_rfc3339(),
            'average_speed': average_speed,
            'location': element['location']
        }

def run(argv=None):
    pipeline_options = PipelineOptions(argv)
    pipeline_options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=pipeline_options) as p:
        (p
         | 'ReadFromPubSub' >> ReadFromPubSub(topic=f'projects/{PROJECT_ID}/topics/traffic-data')
         | 'ParseMessages' >> beam.ParDo(ParsePubSubMessage())
         | 'WindowIntoFixedIntervals' >> beam.WindowInto(beam.window.FixedWindows(60))
         | 'CalculateAverageSpeed' >> beam.ParDo(CalculateAverageSpeed())
         | 'WriteToBigQuery' >> WriteToBigQuery(
             f'{PROJECT_ID}:traffic_data.average_speed',
             schema='timestamp:TIMESTAMP,average_speed:FLOAT,location:STRING',
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
