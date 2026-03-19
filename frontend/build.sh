#!/usr/bin/env -S bash -e

_red="\e[4;91m"
_green="\e[4;92m"
_yellow="\e[4;93m"
_cyan="\e[96m"
_nc="\e[0m"
_title=✨
_task="🛠️ "
_lint=🔍
_test=🧪
_done="✔️ "

clear

echo -e "${_title} ${_red}m00d FRONTEND${_nc} ${_title}\n"

echo -en "${_task} ${_green}Installing dependencies${_nc} ... "
pnpm install --frozen-lockfile
echo -e "${_cyan}Complete${_nc}\n"

echo -e "\n${_lint} ${_green}Linting${_nc}:"
pnpm run lint

echo -e "${_test} ${_green}Testing${_nc}:"
pnpm run test

source docker.sh

echo -e "${_done} ${_yellow}Done${_nc}!\n"

unset _red
unset _green
unset _yellow
unset _cyan
unset _nc
unset _title
unset _task
unset _lint
unset _test
unset _done
