# Rollout Webhooks for experiment killing

Kill a feature experiment when anomalies are detected. This deployable function can map from a webhook to a Rollout `PATCH` API call to kill an experiment and halt a deployment. 

This small function can be deployed via: 

    gcloud functions deploy rollout_webhook --trigger-http --runtime "python37"

And then used as a webhook handler with a variety of log and monitoring services to halt a rollout.io experiment. 

See `main.py` for more info including what parameters are used, and where to customise the kill decision logic if needed beyond the initial webhook.

# Links: 

* https://rollout.io/
* https://support.rollout.io/reference

* https://www.loggly.com/blog/smart-alerts-for-anomaly-detection-and-statistical-aggregations/
* https://www.loggly.com/docs/anomaly-detection/ 
* https://www.loggly.com/docs/alerts-overview/

* https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/outlier-detection-nrql-alert

* https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html
* https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-detection.html
