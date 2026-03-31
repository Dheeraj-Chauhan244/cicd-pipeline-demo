pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up environment...'
                bat 'node --version'
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-demo-app sample-app'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f cicd-demo || exit 0'
                bat 'docker run -d -p 5000:5000 --name cicd-demo cicd-demo-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'curl http://localhost:5000/'
            }
        }
    }
}
stage('Test') {
    steps {
        bat 'copy sample-app\\test-results.xml test-results.xml'
    }
    post {
        always {
            junit 'test-results.xml'
        }
    }
}