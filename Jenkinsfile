pipeline {
    agent any
    tools {
        docker 'docker'
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
                    docker build -t wog:latest .
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker compose up
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
                    docker-compose down
                    docker.push('mydockerhubaccount/my-flask-app')
                }
            }
        }
    }
    post {
        always {
            // Clean up resources, if needed
        }
    }
}
