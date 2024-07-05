# Traffic Data Analysis with Streaming Dataflow

## Overview

This project aims to build a pipeline for handling a workflow where streaming traffic data, including speed metrics, is ingested from Pub/Sub to Dataflow. The data is processed to calculate average speeds and stored in BigQuery. This workflow is managed by Cloud Build and Cloud Functions to ensure efficient and scalable data processing and routing.

### Workflow Details

Data from various sensors is sent to a Pub/Sub topic, which triggers a Cloud Function to publish it to another Pub/Sub topic using the push method. This approach allows for automated and responsive data routing, ensuring timely delivery for further processing or analysis.

## Instructions

### Step 1: Create a Service Account

1. Navigate to IAM & Admin in the Google Cloud Console.
2. Create a new Service Account:
   - Click on "Service Accounts".
   - Click "Create Service Account".
   - Enter a name and description for the service account, then click "Create".
3. Assign the following roles to the Service Account:
   - Cloud Build Editor (`roles/cloudbuild.builds.editor`)
   - Cloud Functions Admin (`roles/functions.admin`)
   - Pub/Sub Editor (`roles/pubsub.editor`)
   - Dataflow Developer (`roles/dataflow.developer`)
   - BigQuery Data Editor (`roles/bigquery.dataEditor`)

### Step 2: Setup Pub/Sub

Create a Pub/Sub topic and subscription setup where data is automatically published from one Pub/Sub topic to another, facilitated by triggering a Cloud Function.

### Step 3: Setup BigQuery

Create a BigQuery Dataset and Table to store the processed traffic data.

### Step 4: Configure Dataflow Job

Create a Dataflow Pipeline that:
- Takes input from Pub/Sub.
- Calculates average speed.
- Stores the results in BigQuery.

### Step 5: Configure Cloud Build

Create a `cloudbuild.yaml` file for building and deploying Cloud Functions and Dataflow jobs.

### Step 6: Create Cloud Function

Implement a Cloud Function (`publish_traffic_data`) to publish traffic data to Pub/Sub.

### Step 7: Build and Deploy

Build and deploy the Cloud Function using:
### Create Cloud Build Trigger

1. Navigate to Cloud Build in the Google Cloud Console.
2. Click "Create Trigger".
3. Select "From YAML file".
4. Upload the `cloudbuild.yaml` file created earlier.

### Step 8: Running the Build

Push changes to your Cloud Function code to the specified branch in your repository.
Cloud Build will automatically trigger a build based on your configured trigger and deploy the updated Cloud Function and Dataflow job.
