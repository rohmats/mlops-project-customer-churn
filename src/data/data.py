import dagshub
dagshub.init(repo_owner='rohmats',
             repo_name='mlops-project-customer-churn',
             mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)