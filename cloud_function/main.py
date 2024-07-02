import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('quixotic-treat-419302', 'traffic-data')

def publish_traffic_data(request):
    request_json = request.get_json()
    if request_json and 'speed' in request_json:
        data = json.dumps(request_json).encode('utf-8')
        future = publisher.publish(topic_path, data)
        return 'Message published.'
    else:
        return 'Invalid request.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
