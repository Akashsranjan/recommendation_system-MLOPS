pipeline{
    agent any

    stages{
        stage("cloning from github...")
        steps{
            script{
                echo 'cloning from github..'
                ccheckout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-anime', url: 'https://github.com/Akashsranjan/recommendation_system-MLOPS.git']])
            }
        }
    }
}