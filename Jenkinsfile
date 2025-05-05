pipeline {
    agent any
    environment {
        // Optional: define any environment variables if needed
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build project using Gradle
                sh './gradlew clean build'
            }
        }
        stage('Test') {
            steps {
                // Run tests using Gradle
                sh './gradlew test'
            }
        }


        
        stage('Publish') {
            steps {
                // Publish to Maven Central or other repository if needed
                sh './gradlew publish'
            }
        }
    }

}
