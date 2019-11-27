pipeline{
    agent{
        dockerfile{
            filename 'Dockerfile'
            args '-u root:root'
        }
    }
    stages{
        stage('Build'){
            steps{
                sh "python --version"
            }
        }
    }
}
