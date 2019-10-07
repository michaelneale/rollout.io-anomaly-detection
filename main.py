from flask import escape

import requests


def rollout_webhook(request):
    """HTTP Cloud Function. Using: http://flask.pocoo.org/docs/1.0/api/#flask.Request

    This will take a webhook and kill the apporopriate rollout experiment (thereby halting the rollout!)

    USAGE and parameters: 
        Query parmeters are used to pass the rollout app and secret details. 
        POST or GET to a URL once deployed as a google function or similar:
            https://DEPLOYED_FUNCTION_URL?secret=API_Token&app_id=YOUR_APP_ID&environment_name=YOUR_ENV_NAME&flag_name=YOUR_FLAGN_AME

    For example: 
        curl -X POST "https://us-central1-micprojects.cloudfunctions.net/rollout_webhook?secret=..&app_id=..&environment_name=..&flag_name=.."

    Rollout setup info: 
        See https://support.rollout.io/reference for details on how to get your app id and api token.

    Google cloud function deploying: 
        gcloud functions deploy rollout_webhook --trigger-http --runtime "python37"    

    """

    request_json = request.get_json(silent=True)
    request_args = request.args

    url = f"https://x-api.rollout.io/public-api/applications/{request_args['app_id']}/{request_args['environment_name']}/experiments/{request_args['flag_name']}"
    headers = {
        'content-type': "application/json",
        'authorization': f"Bearer {request_args['secret']}"
        }
    payload = '[{"op":"replace","path":"/enabled","value":false}]'

    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(response)

    return 'OK'


def kill_experiment(request_json):
    """
     Can make a decision here. For now lets assume the firing with parameter names indicates
     there is a problem. but if you wanted to do processing on the POSTed json data, do it here!
    """
    return True