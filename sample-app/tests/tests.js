stage('Test') {
    steps {
        bat 'node sample-app\\tests\\test.js'
    }
}