pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-application"
        REGISTRY = "my-docker-registry.local"
        DOCKER_BUILDKIT = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/boredanilonel/rgravc.git'
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker tag $IMAGE_NAME:$BUILD_NUMBER $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER'
                sh 'docker push $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $IMAGE_NAME || true
                docker rm $IMAGE_NAME || true
                docker run -d --name $IMAGE_NAME -p 80:80 $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Проверка Docker') {
            steps {
                sh 'docker --version'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
