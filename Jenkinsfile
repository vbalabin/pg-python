node {
    def app

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

    stage('Build image') {
        /* This builds the actual image */

        app = docker.build("thessky/epam-practice")
    }

    stage('Push image') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
        docker.withRegistry('https://registry.hub.docker.com', 'sky-docker-hub') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
    }
}
