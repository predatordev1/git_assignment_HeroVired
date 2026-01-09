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
            emailext (
                subject: "SUCCESS: cicd_flask_app pipeline status",
                body: "Pipeline succeeded. Flask app has been deployed successfully.",
                to: "devendra8182@gmail.com"
            )
        }
        failure {
            echo "Pipeline failed, skipping deployment"
            emailext (
                subject: "FAILURE: cicd_flask_app pipeline failed",
                body: "Pipeline failed. Please check Jenkins console output for details.",
                to: "devendra8182@gmail.com"
            )
        }
    }
}
