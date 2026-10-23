pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                sh 'test -f index.html'
                sh 'test -f test_form.py'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test_form.py'
            }
        }
    }

    post {
        success {
            echo 'All HTML form tests passed!'
        }
        failure {
            echo 'HTML form tests failed.'
        }
    }
}