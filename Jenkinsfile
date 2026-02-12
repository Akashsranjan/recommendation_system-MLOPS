pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage("Cloning from GitHub") {
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

        stage("Create virtual environment") {
            steps {
                script {
                    echo 'Creating virtual environment...'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc[gcs]
                    '''
                }
            }
        }

        stage("DVC Pull") {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo "Running DVC Pull..."

                        sh '''
                        . ${VENV_DIR}/bin/activate

                        echo "Using GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS"
                        ls -l $GOOGLE_APPLICATION_CREDENTIALS || echo "Credentials file not found!"

                        export GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS

                        dvc pull -v
                        '''
                    }
                }
            }
        }
    }
}





// pipeline {
//     agent any

//     environment {
//         VENV_DIR ='venv'
//     }

//     stages {
//         stage("cloning from github") {
//             steps {
//                 script {
//                     echo 'Cloning from GitHub...'
//                     checkout scmGit(
//                         branches: [[name: '*/main']],
//                         extensions: [],
//                         userRemoteConfigs: [[
//                             credentialsId: 'github-token-anime',
//                             url: 'https://github.com/Akashsranjan/recommendation_system-MLOPS.git'
//                         ]]
//                     )
//                 }
//             }
//         }


//         stage("making a virtual environment.....") {
//             steps {
//                 script {
//                     echo 'making a virtual environment.....'
//                     sh '''
//                     python -m venv ${VENV_DIR}
//                     . ${VENV_DIR}/bin/activate
//                     pip install --upgrade pip
//                     pip install -e .
//                     pip install  dvc
//                     '''
                    
//                 }
//             }
//         }

//         stage("DVC Pull"){
//             steps{
//                 withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
//                     script{
//                         echo 'DVC Pul....'
//                         sh '''
//                         . ${VENV_DIR}/bin/activate
//                         dvc pull
//                         '''
//                     }
//                 }
//             }
//         }
//     }
// }
