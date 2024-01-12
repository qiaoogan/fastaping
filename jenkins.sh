# build image
docker build --tag=backendpy:0.0.${BUILD_NUMBER} .

# push image
# do nothing

# deploy
kubectl set image deployment/ezl-backendpy-depl ezl-backendpy=backendpy:0.0.${BUILD_NUMBER}
