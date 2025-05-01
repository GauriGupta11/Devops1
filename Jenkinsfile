pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
        ART_USER = credentials('artifactory-username')
        ART_PASS = credentials('artifactory-password')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/GauriGupta11/Devops1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || poetry install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }

        stage('Build Package') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
            }
        }

        stage('Publish to Artifactory') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'artifactory-credentials', usernameVariable: 'ART_USER', passwordVariable: 'ART_PASS')]) {
                    sh 'curl -u$ART_USER:$ART_PASS -T dist/*.whl "https://trial72qis4.jfrog.io/artifactory/python-local/"'
                }
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
