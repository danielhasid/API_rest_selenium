pipeline {
  agent any
  stages {
    stage('Init') {
      agent any
      steps {
        git(url: 'https://github.com/danielhasid/API_rest_selenium.git', branch: './main')
        build 'backend_testing.py'
      }
    }

  }
}