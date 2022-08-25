#!/bin/bash
# EMBArk - The firmware security scanning environment
#
# Copyright 2020-2022 Siemens Energy AG
# Copyright 2020-2022 Siemens AG
#
# EMBArk comes with ABSOLUTELY NO WARRANTY.
#
# EMBArk is licensed under MIT
#
# Author(s): Benedikt Kuehne

# Description: Helper functions

docker_image_rm(){
  # removes image by name and version
  # $1 name
  # $2 version
  local IMAGE_NAME_="$1"
  local IMAGE_VERSION_="$2"

  if [[ $(docker image ls -q "$IMAGE_NAME_"":""$IMAGE_VERSION_" | wc -c ) -ne 0 ]] ; then
    if [[ $(docker ps -a -q --filter "ancestor=""$IMAGE_NAME_"":""$IMAGE_VERSION_" | wc -c) -ne 0 ]]; then
      local CONTAINERS_
      mapfile -t CONTAINERS_ < <(docker ps -a -q --filter ancestor="$IMAGE_NAME_"":""$IMAGE_VERSION_" --format="{{.ID}}")
      for CONTAINER_ID_ in "${CONTAINERS_[@]}" ; do
        echo -e "$GREEN""$BOLD""Stopping ""$CONTAINER_ID_"" docker container""$NC"
        docker stop "$CONTAINER_ID_"
        echo -e "$GREEN""$BOLD""Remove ""$CONTAINER_ID_"" docker container""$NC"
        docker container rm "$CONTAINER_ID_" -f
      done
    fi
    echo -e "$GREEN$BOLD""Removing ""$IMAGE_NAME_"":""$IMAGE_VERSION_" "docker image""$NC\\n"
    docker image rm "$IMAGE_NAME_"":""$IMAGE_VERSION_" -f
  fi
}

docker_network_rm(){
  # removes docker networks by name
  local NET_ID
  if docker network ls | grep -E "$1"; then
    echo -e "\n$GREEN""$BOLD""Found ""$1"" - removing it""$NC"
    NET_ID=$(docker network ls | grep -E "$1" | awk '{print $1}')
    echo -e "$GREEN""$BOLD""Remove ""$1"" network""$NC"
    docker network rm "$NET_ID" 
  fi
}

copy_file(){
  # check and copy file forcing overwrite
  # $1 : source
  # $2 : destination
  if ! [[ -f "$1" ]] ; then
    echo -e "\\n$RED""Could not find ""$1""$NC\\n"
  elif  ! [[ -d "$2" ]] || ! [[ -f "$2" ]] ; then
    echo -e "\\n$RED""Could not find ""$2""$NC\\n"
  fi
  cp -f "$1" "$2"
}

enable_strict_mode() {
  local STRICT_MODE_="$1"

  if [[ "$STRICT_MODE_" -eq 1 ]]; then
    # http://redsymbol.net/articles/unofficial-bash-strict-mode/
    # https://github.com/tests-always-included/wick/blob/master/doc/bash-strict-mode.md
    # shellcheck disable=SC1091
    source ./helper/wickStrictModeFail.sh
    set -e          # Exit immediately if a command exits with a non-zero status
    set -u          # Exit and trigger the ERR trap when accessing an unset variable
    set -o pipefail # The return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status
    set -E          # The ERR trap is inherited by shell functions, command substitutions and commands in subshells
    shopt -s extdebug # Enable extended debugging
    IFS=$'\n\t'     # Set the "internal field separator"
    trap 'wickStrictModeFail $? | tee -a /tmp/embark_error.log' ERR  # The ERR trap is triggered when a script catches an error

    echo -e "[!] INFO: EMBArk STRICT mode enabled!"

  fi
}
