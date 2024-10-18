from googleapiclient.discovery import build
import base64
import google.auth
import os

def hello_pubsub():   
 
    service = build('dataflow', 'v1b3')
    project = "smart-mark-438604-n2"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "cricbuzz_job",  # Provide a unique name for the job
        "parameters": {
            "inputFilePattern": "gs://airflow-cricbuzz-akhilproject1/batsmen_rankings.csv",
            "JSONPath": "gs://cricbuzz-metadata/batsmen_ranking.json",
            "outputTable": "smart-mark-438604-n2:cricbuzz_data.cricbuzz_ODI_ranking",
            "bigQueryLoadingTemporaryDirectory": "gs://cricbuzz-metadata",
            "javascriptTextTransformGcsPath": "gs://cricbuzz-metadata/udf.js",
            "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

hello_pubsub()