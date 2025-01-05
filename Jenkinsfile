pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'localhost:30000'  // Replace with your Docker registry URL
        APP_NAME = 'hello-world'
        DOCKER_IMAGE = "${DOCKER_REGISTRY}/${APP_NAME}:latest"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                    helm upgrade --install $APP_NAME C:\helm \
                        --set image.repository=$DOCKER_REGISTRY \
                        --set image.tag=latest \
                        --set image.pullPolicy=Always
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
