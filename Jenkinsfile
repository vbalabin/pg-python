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

        stage('Push'){
            agent any
            steps{
                script{
                    def app
                    app = docker.build("thessky/epam-practice")
                    docker.withRegistry('https://registry.hub.docker.com', 'sky-docker-hub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                        } 
                    echo "Trying to Push Docker Build to DockerHub"
                }
            }
        }
    }

    post {
        always {
            echo "congratz"
        }
    }
}
