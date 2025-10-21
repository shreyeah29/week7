pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📦 Cloning repository..."
                checkout scm
            }
        }

        stage('Check Files') {
            steps {
                sh 'ls -R'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh 'docker build -t shreyeah29/week7-myapp:latest -f Dockerfile .'
            }
        }

        stage('Run Container Test') {
            steps {
                echo "🚀 Running container to verify build..."
                sh '''
                    docker stop temp-week7 || true
                    docker rm temp-week7 || true
                    docker run -d -p 5011:5001 --name temp-week7 shreyeah29/week7-myapp:latest
                    sleep 5
                    docker ps
                    docker stop temp-week7
                    docker rm temp-week7
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "📤 Pushing image to Docker Hub..."
                sh '''
                    echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin
                    docker push shreyeah29/week7-myapp:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully – Image pushed to Docker Hub!"
        }
        failure {
            echo "❌ Pipeline failed. Please check the logs."
        }
    }
}
