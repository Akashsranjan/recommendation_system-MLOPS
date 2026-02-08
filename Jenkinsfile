pipeline {
    agent any

    stages {
        stage("cloning from github") {
            steps {
                script {
                    echo 'Cloning from GitHub...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token-anime',
                            url: 'https://github.com/Akashsranjan/recommendation_system-MLOPS.git'
                        ]]
                    )
                }
            }
        }
    }
}
