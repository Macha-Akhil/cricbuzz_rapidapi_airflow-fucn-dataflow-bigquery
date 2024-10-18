# POST /v1b3/projects/smart-mark-438604-n2/locations/us-central1/templates:launch?gcsPath=gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery
# {
#     "jobName": "cricbuzz_job",
#     "environment": {
#         "bypassTempDirValidation": false,
#         "numWorkers": 2,
#         "tempLocation": "gs://cricbuzz-metadata/temp",
#         "ipConfiguration": "WORKER_IP_UNSPECIFIED",
#         "enableStreamingEngine": false,
#         "additionalExperiments": [
#             "use_runner_v2"
#         ],
#         "additionalUserLabels": {}
#     },
#      "parameters": {
#         "inputFilePattern": "gs://airflow-cricbuzz-akhilproject1/batsmen_rankings.csv",
#         "JSONPath": "gs://cricbuzz-metadata/batsmen_ranking.json",
#         "outputTable": "smart-mark-438604-n2:cricbuzz_data.cricbuzz_ODI_ranking",
#         "bigQueryLoadingTemporaryDirectory": "gs://cricbuzz-metadata",
#         "javascriptTextTransformGcsPath": "gs://cricbuzz-metadata/udf.js",
#         "javascriptTextTransformFunctionName": "transform"
#     }
# }