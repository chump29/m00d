#!/usr/bin/env -S bash -e

_frontend_url="https://git.postfmly.com/api/v1/packages/$GITHUB_VAULT_USER/container/m00d-frontend/"
_backend_url="https://git.postfmly.com/api/v1/packages/$GITHUB_VAULT_USER/container/m00d-backend/"

_token=$(curl --request GET \
  --location \
  --silent \
  --fail \
  --url https://vault.postfmly.com/v1/kv/data/github \
  --header "X-Vault-Token: $GITHUB_VAULT_TOKEN" \
  | jq -r .data.data.key)

echo -e "✨ m00d Packages ✨\n"

for _pkg in latest amd64 arm64; do
  echo -e "   ╰› Deleting ${_pkg^^} frontend package"
  curl --request DELETE \
    --location \
    --silent \
    --fail \
    --url "${_frontend_url}${_pkg}" \
    --header "authorization: token $_token" \
    --output /dev/null

  echo -e "   ╰› Deleting ${_pkg^^} backend package"
  curl --request DELETE \
    --location \
    --silent \
    --fail \
    --url "${_backend_url}${_pkg}" \
    --header "authorization: token $_token" \
    --output /dev/null

  echo
done

echo -e "✔️  Done"

unset _frontend_url
unset _backend_url
unset _token
