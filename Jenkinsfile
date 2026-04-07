pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'git@github.com:08pradeep/flask-app-1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pradeep0802/flask-app:v1 .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}
