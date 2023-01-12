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
        sh 'python3 https://github.com/danielhasid/API_rest_selenium.git rest_app.py'
      }
    }

    stage('web_app') {
      steps {
        sh 'python3 https://github.com/danielhasid/API_rest_selenium.git web_app.py'
      }
    }

    stage('backend_testing') {
      steps {
        sh 'python3 https://github.com/danielhasid/API_rest_selenium.git backend_testing.py'
      }
    }

    stage('frontend _testing') {
      steps {
        sh 'python3 https://github.com/danielhasid/API_rest_selenium.git frontend _testing.py'
      }
    }

    stage('clean_environment') {
      steps {
        sh 'python3 https://github.com/danielhasid/API_rest_selenium.git clean_environment.py'
      }
    }

  }
}
