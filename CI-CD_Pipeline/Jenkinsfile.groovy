pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Clone Github Repo') {
            steps {
                sh '''
                    git clone -b main https://github.com/predatordev1/git_assignment_HeroVired.git
                '''
            }
        }
        stage('Installation of flask') {
            steps {
                sh '''
                    pip3 install flask
                '''
            }
        }
        stage('Testing of flask app') {
            steps {
                sh '''
                    cd git_assignment_HeroVired/CI-CD_Pipeline
                    python3 ./ci_cd_app.py &
                    sleep 5
                    curl -f http://localhost:5000 || exit 1
                    pkill -f ci_cd_app.py
                '''
            }
        }
    }
    post {
        success {
            echo "Flask app works good, deploying now..."
            sh '''
                cp git_assignment_HeroVired/CI-CD_Pipeline/ci_cd_app.py \
                   git_assignment_HeroVired/CI-CD_Pipeline/cicd_logs/
            '''
        }
        failure {
            echo "Pipeline failed, skipping deployment"
        }
    }
}
