pipeline{
    agent{
        docker{
            image 'python:3.7.5-stretch'
        }
    }
    stages{
        stage('Build'){
            steps{
                python --version
                python print("hello there")
            }
        }
    }
    post{
        always{
            print("this will always run")
        }
        success{

        }
        failure{

        }
        unstable{

        }
        changed{

        }
    }
}