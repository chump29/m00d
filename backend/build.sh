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

echo -e "${_title} ${_red}m00d BACKEND${_nc} ${_title}\n"

echo -en "${_task} ${_yellow}Installing dependencies${_nc} ... "
uv sync --extra dev --quiet
echo -e "${_cyan}Complete${_nc}\n"

echo -e "${_lint} ${_yellow}Linting${_nc}:\n"
source lint.sh

echo -e "\n${_test} ${_yellow}Testing${_nc}:\n"
source test.sh

source docker.sh

echo -e "\n${_done} ${_green}Done${_nc}!\n"

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
