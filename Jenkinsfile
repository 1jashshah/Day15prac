pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.11'
    }

    stages {
        stage("Clone Repo") {
            steps {
                // Clone the repository
                git url: 'https://github.com/1jashshah/Day15prac.git', branch: 'main'
            }
        }

        stage("Build") {
            steps {
                script {
                    // Execute the Python script
                    sh "python${PYTHON_VERSION} todo.py"
                }
            }
        }

        stage("Archive Artifacts") {
            steps {
                // Archive all Python files
                archiveArtifacts artifacts: '**/*.py', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo "BUILD COMPLETED"
        }
        success {
            echo "Build Succeeded"
        }
        failure {
            echo "Build Failed"
        }
    }
}
