import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('quixotic-treat-419302', 'traffic-data')

def publish_traffic_data(request):
    if isinstance(request, dict):
        data = json.dumps(request).encode('utf-8')
        future = publisher.publish(topic_path, data)
        return 'Message published.'
    else:
        return 'Invalid request.', 400

