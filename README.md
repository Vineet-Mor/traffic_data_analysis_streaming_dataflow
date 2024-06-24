# traffic_data_analysis_streaming_dataflow
To build a pipeline to handle workflow where streaming traffic data (including speed) is ingested from Pub/Sub to Dataflow, processed to calculate the average speed, and then stored in BigQuery. This workflow will be managed by Cloud Build and Cloud Functions.

Instructions:
Step 1: Create a Service Account
Navigate to IAM & Admin:
- Open the Google Cloud Console and go to the IAM & Admin section.
- Create a New Service Account:
- Click on "Service Accounts".
- Click "Create Service Account".
- Enter a name and description for the service account, then click "Create".
- Assign Roles to the Service Account:
  - Cloud Build Editor (roles/cloudbuild.builds.editor)
  - Cloud Functions Admin (roles/functions.admin)
  - Pub/Sub Editor (roles/pubsub.editor)
  - Dataflow Developer (roles/dataflow.developer)
  - BigQuery Data Editor (roles/bigquery.dataEditor)
-Click "Done".

Step 2: Setup Pub/Sub
Create a Pub/Sub Topic and Subscription.

Step 3: Setup BigQuery
Create a BigQuery Dataset and Table

Step 4: Configure Dataflow Job
Create a Dataflow Pipeline that takes the input from Pub/Sub, calculate the average speed and store the results in BigQuery.

Step 5: Configure Cloud Build
Create a cloudbuild.yaml file.

Step 6: Create Cloud Function
Create a Cloud Function to publish traffic data to Pub/Sub.

Step 7: Build and Deploy
Build and Deploy the Cloud Function using "gcloud functions deploy publish_traffic_data".
Create Cloud Build Trigger:
- Navigate to Cloud Build in the Google Cloud Console.
- Click "Create Trigger".
- Select "From YAML file".
- Upload the cloudbuild.yaml file created earlier.

Step 8: Running the Build:
- Push your Cloud Function code changes to the specified branch in your repository.
- Cloud Build will automatically trigger a build based on your configured trigger and deploy the updated Cloud Function and Dataflow job.

