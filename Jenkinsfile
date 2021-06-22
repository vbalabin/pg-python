pipeline {
    agent any 
    stages {
        stage('Test') { 
            agent { 
                docker {
                    image "python:3.8"
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "ls"
                    sh "pip install -r requirements.txt --user"
                    sh 'python -m pytest --junit-xml test-reports/results.xml tests/test_practice.py'
                }
            }
        }
    }

    post {
        always {
            junit 'test-reports/results.xml'
        }
    }
}
