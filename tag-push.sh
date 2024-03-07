#!/bin/bash
#Push image to local registry
IMAGE="$1"
DIRECTORY=localhost:5050
TAG="$2"

docker tag "$IMAGE:$TAG" "$DIRECTORY/$IMAGE:$TAG"
docker push "$DIRECTORY/$IMAGE:$TAG"
