# build image
docker build --tag=backendpy:0.0.${BUILD_NUMBER} .

# push image
# do nothing

# deploy
kubectl apply -f ./deployment/configMap.yaml
kubectl patch configmap/fastaping-config \
    --type merge \
    -p "{\"data\":{\"FASTAPING_VERSION\":\"0.0.${BUILD_NUMBER}\"}}"
kubectl apply -f ./deployment/deploysvc.yaml
kubectl set image deployment/ezl-backendpy-depl ezl-backendpy=backendpy:0.0.${BUILD_NUMBER}

