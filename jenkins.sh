# build image
docker build --tag=backendpy:0.0.${BUILD_NUMBER} .

# push image
# do nothing

# deploy
export FASTAPING_VERSON=0.0.${BUILD_NUMBER}
kubectl apply -f ./deployment/deploysvc.yaml --env=FASTAPING_VERSION=0.0.${BUILD_NUMBER}
# kubectl set image deployment/ezl-backendpy-depl ezl-backendpy=backendpy:0.0.${BUILD_NUMBER}
