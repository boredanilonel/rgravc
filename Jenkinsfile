pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = "my-application"
        REGISTRY = "my-docker-registry.local"
        BUILD_TAG = "${IMAGE_NAME}:${BUILD_NUMBER}"
        FULL_IMAGE_NAME = "${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Клонирование репозитория
                git branch: 'main', url: 'https://github.com/boredanilonel/rgravc.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Сборка Docker-образа
                sh '''
                docker build -t $BUILD_TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                // Тэгирование и пуш образа в реестр
                sh '''
                docker tag $BUILD_TAG $FULL_IMAGE_NAME
                docker push $FULL_IMAGE_NAME
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                // Деплой контейнера
                sh '''
                docker stop $IMAGE_NAME || true
                docker rm $IMAGE_NAME || true
                docker run -d --name $IMAGE_NAME -p 80:80 $FULL_IMAGE_NAME
                '''
            }
        }

        stage('Проверка Docker') {
            steps {
                // Проверка версии Docker
                sh 'docker --version'
            }
        }
    }

    post {
        always {
            // Очистка рабочей директории
            cleanWs()
        }
    }
}
