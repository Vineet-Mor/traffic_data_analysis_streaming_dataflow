# Pub/Sub Traffic Data Publisher

This repository contains a Google Cloud Function that publishes traffic data to a Pub/Sub topic. The function is triggered via an HTTP request and publishes the received data to the specified Pub/Sub topic.

## Function Overview

The `publish_traffic_data` function performs the following steps:
1. **Initialize Pub/Sub Publisher Client**:
    - A Pub/Sub publisher client is created using `pubsub_v1.PublisherClient()`.
    - The target Pub/Sub topic is specified as `projects/quixotic-treat-419302/topics/traffic-data`.

2. **Publish Data to Pub/Sub**:
    - The function expects the request to be in dictionary format.
    - The request data is converted to a JSON string and encoded to bytes.
    - The encoded data is published to the Pub/Sub topic.
    - If the data is successfully published, the function returns a success message.
    - If the request is not a valid dictionary, the function returns an error message.
