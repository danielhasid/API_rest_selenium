pipeline {
  agent any
  stages {
    stage('pull_code') {
      steps {
        sh 'git pull'
      }
    }

    stage('run_rest_app') {
      steps {
        sh 'python3 rest_app.py'
        sh 'python3 web_app.py'
      }
    }

  }
}