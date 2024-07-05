# Cloud Build Configuration for Traffic Data Processing

This repository contains the Cloud Build configuration for deploying a Cloud Function and a Dataflow job for processing traffic data. The build process includes steps for building a Docker image, deploying the Cloud Function, and running the Dataflow job.

## Cloud Build YAML Overview

The `cloudbuild.yaml` file performs the following steps:

1. **Build Docker Image**:
    - Uses the `docker` builder to build a Docker image.
    - Tags the image as `gcr.io/$PROJECT_ID/my-function:latest`.
    
    ```yaml
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-function:latest', '.']
    ```

2. **Deploy Cloud Function**:
    - Uses the `gcloud` builder to deploy the Cloud Function.
    - Specifies the runtime as `python39`.
    - Sets the trigger to HTTP and allows unauthenticated access.
    - Deploys the function from the current directory (`--source`, '.').
    
    ```yaml
    - name: 'gcr.io/cloud-builders/gcloud'
      args: ['functions', 'deploy', 'my-function',
             '--runtime', 'python39',
             '--trigger-http',
             '--allow-unauthenticated',
             '--source', '.']
    ```

3. **Run Dataflow Job**:
    - Uses the `gcloud` builder to run a Dataflow job.
    - Specifies the GCS location of the Dataflow job script.
    - Sets the region to `us-central1`.
    - Passes parameters for the input Pub/Sub topic and output BigQuery table.
    
    ```yaml
    - name: 'gcr.io/cloud-builders/gcloud'
      args: ['dataflow', 'jobs', 'run', 'traffic-dataflow-job',
             '--gcs-location', 'gs://traffic_staging/dataflow_job.py',
             '--region', 'us-central1',
             '--parameters', 'inputTopic=projects/quixotic-treat-419302/topics/traffic-data,outputTable=quixotic-treat-419302:traffic_data.average_speed']
    ```

4. **Substitutions**:
    - Defines a substitution for the project ID.
    
    ```yaml
    substitutions:
      _PROJECT_ID: "quixotic-treat-419302"
    ```
5. **Options**:
    - `logging`: Set to `CLOUD_LOGGING_ONLY` to specify logging behavior.
    - `logsBucket`: Specifies the Cloud Storage bucket `gs://newbucketvm` for storing logs.


6. **Triggers**:
    - Sets up a trigger for GitHub commits to the main branch.
    - Runs the Dataflow job when changes are pushed to the main branch.
    
    ```yaml
    triggers:
    - github:
        branch: main
        build:
          step: - name: 'gcr.io/cloud-builders/gcloud'
                  args: ['dataflow', 'jobs', 'run', 'traffic-dataflow-job',
                         '--gcs-location', 'gs://traffic_staging/dataflow_job.py',
                         '--region', 'us-central1',
                         '--parameters', 'inputTopic=projects/quixotic-treat-419302/topics/traffic-data,outputTable=quixotic-treat-419302:traffic_data.average_speed']
    ```
