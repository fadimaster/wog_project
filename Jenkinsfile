pipeline {
    agent any
    tools {
        dockerTool 'latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t fadimaster/wog:latest .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                   sh 'docker-compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements-test.txt'
                    sh 'python tests/e2e.py'
                }
            }
        }
        stage('Publish') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
                    sh 'docker login -u ${DOCKER_REGISTRY_USER} -p ${DOCKER_REGISTRY_PWD}'
                    sh 'docker push fadimaster/wog:latest'
                }
            }
        }
    }
    post {
        always {
            sh 'docker-compose down'
            sh 'docker rmi fadimaster/wog:latest'
        }
    }
}
