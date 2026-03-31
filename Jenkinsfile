pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'cicd-demo-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        REGISTRY = 'docker.io'  // Change to your registry
    }
    
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
                sh '''
                    echo "Python version:"
                    python --version
                    echo "Docker version:"
                    docker --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                dir('sample-app') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                dir('sample-app') {
                    sh '''
                        pip install pytest pytest-cov
                        pytest tests/ -v --junitxml=test-results.xml --cov=src --cov-report=xml
                    '''
                }
            }
            post {
                always {
                    junit 'sample-app/test-results.xml'
                    publishHTML([
                        reportDir: 'sample-app',
                        reportFiles: 'coverage.xml',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}", "./sample-app")
                }
            }
        }
        
        stage('Test Docker Image') {
            steps {
                echo 'Testing Docker container...'
                script {
                    docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").inside {
                        sh 'python -c "import requests; print(requests.get(\"http://localhost:5000/\").json())"'
                    }
                }
            }
        }
        
        stage('Push to Registry') {
            when {
                branch 'main'
            }
            steps {
                echo 'Pushing image to registry...'
                script {
                    docker.withRegistry("https://${env.REGISTRY}", 'dockerhub-credentials') {
                        docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").push()
                        docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").push("latest")
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application...'
                script {
                    // Stop and remove existing container
                    sh '''
                        docker stop cicd-demo-app || true
                        docker rm cicd-demo-app || true
                    '''
                    
                    // Run new container
                    sh """
                        docker run -d \
                            --name cicd-demo-app \
                            -p 5000:5000 \
                            --restart unless-stopped \
                            ${env.DOCKER_IMAGE}:${env.DOCKER_TAG}
                    """
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment...'
                script {
                    def maxAttempts = 10
                    def attempt = 0
                    def deployed = false
                    
                    while (attempt < maxAttempts && !deployed) {
                        attempt++
                        try {
                            def response = sh(script: 'curl -s http://localhost:5000/health', returnStdout: true).trim()
                            if (response.contains('healthy')) {
                                deployed = true
                                echo '✅ Deployment verified successfully!'
                            }
                        } catch (Exception e) {
                            echo "Attempt ${attempt}/${maxAttempts}: Waiting for deployment..."
                            sleep 5
                        }
                    }
                    
                    if (!deployed) {
                        error 'Deployment verification failed!'
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            // Send notification (email, Slack, etc.)
        }
        failure {
            echo 'Pipeline failed!'
            // Send failure notification
        }
        always {
            cleanWs() // Clean workspace
        }
    }
}