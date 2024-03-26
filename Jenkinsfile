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
                    sh 'docker build -t wog:latest .'
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
            sh 'docker rmi wog:latest'
        }
    }
}
