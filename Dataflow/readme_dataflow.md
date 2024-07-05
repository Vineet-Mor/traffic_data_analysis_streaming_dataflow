# Dataflow Pipeline for Traffic Data Processing

This repository contains a Dataflow pipeline that processes traffic data from a Pub/Sub topic, calculates the average speed within fixed time windows, and writes the results to a BigQuery table.

## Pipeline Flow

1. **Data Ingestion from Pub/Sub**:
    - The pipeline begins by reading real-time traffic data from a Pub/Sub topic.
    - The Pub/Sub topic is specified as `projects/{PROJECT_ID}/topics/traffic-data`.

2. **Message Parsing**:
    - The raw messages from Pub/Sub are parsed from JSON format.
    - A custom `DoFn` named `ParsePubSubMessage` is used to decode the JSON messages into Python dictionaries.

3. **Windowing**:
    - The parsed data is divided into fixed windows of 60 seconds.
    - This is achieved using `beam.WindowInto(beam.window.FixedWindows(60))`.
    - Windowing helps in processing the data in manageable chunks and facilitates time-based aggregations.

4. **Calculation of Average Speed**:
    - Within each 60-second window, the pipeline calculates the average speed of the vehicles.
    - A custom `DoFn` named `CalculateAverageSpeed` performs this calculation.
    - The output is a dictionary containing the timestamp (window end time), the average speed, and the location.

5. **Writing to BigQuery**:
    - The processed data is written to a BigQuery table.
    - The table schema includes `timestamp`, `average_speed`, and `location`.
    - The data is appended to the BigQuery table specified as `projects/{PROJECT_ID}/datasets/traffic_data/tables/average_speed`.
