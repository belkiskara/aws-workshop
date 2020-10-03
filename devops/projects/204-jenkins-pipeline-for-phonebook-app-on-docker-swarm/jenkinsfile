pipeline{
    agent { label "master" }
    environment {
        ECR_REGISTRY = ""
    }
    stages {
        stage('Create ECR Repo') {
            steps {
            echo 'Creating ECR Repository'
            }
        }
        stage('Build App Docker Images'){
            steps {
                echo 'Building app Docker images'
            }
        }
        stage('Push Docker Images to ECR Repo'){
            steps {
                echo 'Pushing images to ECR'
            }
        }
        stage('Create Infrastructure for the App'){
            steps {
                echo 'Creating Docker Swarm'
            }
        }
        stage('Test the Infrastructure'){
            steps {
                echo 'Testing if Docker Swarm is ready or not'
            }
        }
        stage('Deploy the App on Docker Swarm'){
            steps {
                echo 'Deploying the app'
            }
        }
        stage('Test the application'){
            steps {
                echo 'Check if the application is ready or not'
            }
        }
    }
    post {
        always {
            echo 'Deleting all local images'
        }
        failure {
            echo 'Deleting the image repository on ECR due to failure'
            echo 'Deleting the cloudformation stack due to failure'
        }
    }
}