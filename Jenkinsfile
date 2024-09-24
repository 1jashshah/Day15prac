pipeline{
    agent any
    environment{
        PYTHON_VERSION = '3.11'
    }

    stages{
        stage("CLone Repo"){
            steps{
                git url: 'https://github.com/1jashshah/Day15prac.git', branch: 'main'
            }
        }
    }
    
    stages{
        stage("Build"){
            steps{
                script{
                    sh 'python3 todo.py'
                }
            }
        }
    }

    stages{
        stage("Archive Artifacts"){
            archiveArtifacts artifacts: '**/*.py', allowEmptyArchieve:true
        }
    }

    post{
        always {
             echo " BUILD COMPLETED"
        }
        success {
            echo "Build Succeed"
        }
        failure{
            echo "build failed"
        }
    }
}
