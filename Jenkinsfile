pipeline {
    agent any
    tools {
        dockerTool 'docker'
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
                   sh 'docker-compose up'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Assuming Python and Selenium are set up in Jenkins environment
                    sh 'python3 e2e.py'
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
        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }
    post {
        always {
            sh 'docker rmi fadimaster/wog:latest'
        }
    }
}
