#!/bin/sh

ENVIRONMENT_NAME=Production
FLAG_NAME=spankyChat

# Remember to set up the app id and secret
# docs: https://support.rollout.io/reference#authentication

curl --request PATCH \
  --url https://x-api.rollout.io/public-api/applications/$ROX_APP_ID/$ENVIRONMENT_NAME/experiments/$FLAG_NAME \
  --header "authorization: Bearer $ROX_SECRET_KEY" \
  --header 'content-type: application/json' \
  --data '[{"op":"replace","path":"/enabled","value":false}]'
