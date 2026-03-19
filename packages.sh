#!/usr/bin/env -S bash -e

TERM=xterm-256color

clear

_frontend_url="https://git.postfmly.com/api/v1/packages/$GITHUB_VAULT_USER/container/m00d-frontend/"
_backend_url="https://git.postfmly.com/api/v1/packages/$GITHUB_VAULT_USER/container/m00d-backend/"

_token=$(curl --request GET \
  --location \
  --silent \
  --url https://vault.postfmly.com/v1/kv/data/github \
  --header "X-Vault-Token: $GITHUB_VAULT_TOKEN" \
  | jq -r .data.data.key)

_green="\e[1;92m"
_yellow="\e[93m"
_nc="\e[0m"

echo -e "✨ ${_green}m00d Packages${_nc} ✨\n"

for _pkg in latest amd64 arm64; do
  echo -e "   ╰› ${_yellow}Deleting ${_pkg^^} frontend package${_nc}"
  curl --request DELETE \
    --location \
    --silent \
    --url "${_frontend_url}${_pkg}" \
    --header "authorization: token $_token" \
    --output /dev/null

  echo -e "   ╰› ${_yellow}Deleting ${_pkg^^} backend package${_nc}"
  curl --request DELETE \
    --location \
    --silent \
    --url "${_backend_url}${_pkg}" \
    --header "authorization: token $_token" \
    --output /dev/null

  echo
done

echo -e "✔️  ${_green}Done${_nc}"

unset _frontend_url
unset _backend_url
unset _token
unset _green
unset _yellow
unset _nc
