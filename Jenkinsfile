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
                    sh 'python -m pytest tests/test_practice.py'
                }
            }
        }
    }

    node {
        stage('Clone repository') {
            /* Cloning the Repository to our Workspace */

            echo "Clone Rep"
        }
    }

    post {
        always {
            echo "congratz"
        }
    }
}
