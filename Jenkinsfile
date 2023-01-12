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

    stage('web_app') {
      steps {
        sh 'python3 web_app.py'
      }
    }

    stage('backend_testing') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }

    stage('frontend _testing') {
      steps {
        sh 'python3 frontend _testing.py'
      }
    }

    stage('combined_testing') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }

  }
}