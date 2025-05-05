pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat 'gradlew.bat clean build'

            }
        }
        stage('Test') {
            steps {
                sh 'gradle test'
            }
        }
        stage('Publish') {
            steps {
                sh 'gradle publish'
            }
        }
    }
}
