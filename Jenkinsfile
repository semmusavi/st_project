pipeline {
    agent any

    environment {
        // Define environment variables if needed
        MAVEN_HOME = tool 'Maven' // Maven tool configured in Jenkins
        JAVA_HOME = tool 'Java' // Java tool configured in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from your Git repository
                // Adjust the repository URL and credentials if needed
                git branch: 'main', url: 'https://github.com/semmusavi/st_project'
            }
        }

        stage('Build') {
            steps {
                // Set up JDK and Maven
                bat "set JAVA_HOME=${env.JAVA_HOME}"
                bat "set PATH=%MAVEN_HOME%\\bin;%PATH%"
                
                // Build your Maven project
                bat "mvn clean package"
            }
        }

        stage('Test') {
            steps {
                // Run your tests
                bat "mvn test"
            }
        }

        stage('Deploy') {
            steps {
                // Perform deployment steps here
                // This could be copying artifacts to a server, publishing to a repository, etc.
                // Adjust this based on your deployment strategy
            }
        }
    }

    post {
        always {
            // Cleanup steps or actions to perform after the pipeline completes
        }
    }
}
