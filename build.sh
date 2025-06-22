#!/bin/bash

while getopts t: flag
do
    case "${flag}" in
        t) tag=${OPTARG};;
    esac
done

if [ -z "$tag" ]; then
  echo "Необходимо указать тег с помощью -t"
  exit 1
fi

docker build -t web_upp_web:$tag .
