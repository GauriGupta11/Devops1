pipeline {
    agent any
    triggers {
        githubPush()  // Or use Bitbucket/GitLab equivalent
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh './gradlew clean build'
            }
        }
        stage('Publish Artifact') {
            steps {
                sh './gradlew publish'
            }
        }
    }
    post {
        success {
            echo 'Build and artifact publish successful.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
