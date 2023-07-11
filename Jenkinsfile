pipeline {
    agent any

    stages {
        stage('Checking Out') {
            steps {
                echo '**Pulling Repository**'
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jamesbarker15/f1-twitter-bot.git']])
            }
        }
        stage('Send Files Over SSH') {
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [
                    sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false,
                                makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+',
                                remoteDirectory: '/f1winners', remoteDirectorySDF: false,
                                sourceFiles: 'main.py, data.db, README.md')
                ])])
            }
        }
        stage('Exit Server') {
            steps {
                echo 'Closing Connection....'
            }
        }
    }
}
