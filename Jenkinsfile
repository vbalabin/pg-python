pipeline {
    agent none 
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
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
                }
                post {
                    always {
                        junit 'test-reports/results.xml'
                    }
                }
            }
        }
    }
}
