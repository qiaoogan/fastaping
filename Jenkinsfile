pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build for placeholder'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'git@github.com:qiaoogan/fastaping.git']])
                sh "pwd & ls"
                sh "echo $USER & docker -v & kubectl version"
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Unit Test for placeholder'
            }
        }
        stage('Package') {
            steps {
                echo 'Package for placeholder'
                sh "docker build --tag=backendpy:0.0.${BUILD_NUMBER} ."
                sh "docker image ls"
            }
        }
        stage('Push Image') {
            steps {
                echo 'Push image for placeholder'
            }
        }
        stage('Deploy Dev') {
            steps {
                echo 'Deploy Dev for placeholder'
                sh "kubectl apply -f ./deployment/configMap.yaml"
                sh """kubectl patch configmap/fastaping-config \
                    --type merge \
                    -p '{\"data\":{\"FASTAPING_VERSION\":\"0.0.${BUILD_NUMBER}\"}}'"""
                sh "kubectl apply -f ./deployment/deploysvc.yaml"
                sh "kubectl set image deployment/ezl-backendpy-depl ezl-backendpy=backendpy:0.0.${BUILD_NUMBER}"
            }
        }
        stage('API Tests') {
            steps {
                echo 'API tests for placeholder'
            }
        }
        stage('Deploy UAT') {
            steps {
                echo 'Deploy UAT for placeholder'
            }
        }
    }
}
