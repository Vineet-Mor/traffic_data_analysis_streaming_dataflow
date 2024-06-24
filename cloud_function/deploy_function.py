gcloud functions deploy publish_traffic_data \
    --runtime python39 \
    --trigger-http \
    --allow-unauthenticated \
    --source .
