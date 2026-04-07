pipeline {
    agent any
    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config' // Jenkins user's kubeconfig
    }
    stages {
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
        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods -o wide'
                sh 'kubectl get svc'
            }
        }
    }
}
