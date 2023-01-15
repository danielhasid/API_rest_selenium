pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/danielhasid/API_rest_selenium.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'rest_app.py'
                    } else {
                        sh 'rest_app.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}
