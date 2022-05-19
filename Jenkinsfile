pipeline {
    agent any

    environment {
       RELEASE = "${env.BRANCH_NAME == "release/sprint/" || env.BRANCH_NAME == "develop"}"
        DEPLOY_TO = "${env.BRANCH_NAME == "release/sprint/" ? "release" : ""}"
    }
    
    stages {

        stage('Develop Deployment') {
                when { branch "develop" }
                steps {
                        sh 'echo Started DEV release'
                    }
                }

            // when { branch pattern: "main", comparator: "REGEXP"}
            // when { expression { params.BRANCH_NAME == 'main' } }
            // when { expression { env.DEPLOY_TO == "release" } }
        stage('Release Deployment') {
               when { branch "release/sprint/*" }            
            
                stages('Release Deployment Flow') {

                stage('Approval to QA') {
                    // no agent is used, so executors are not used up when waiting for approvals
                    
                    agent none
                    steps {
                       
                        script {       
                            // properties([parameters([choice(choices: ['Release', 'Hotfix'], description: 'Please select the way of Deployment', name: 'ENVIRONMENT')])])
                            // when {expression { params.ENVIRONMENT == 'Release' } }
                            // def INPUT_PARAMS = input message: 'Approval for Release Deployment', ok: 'Next', parameters: [choice(name: 'ENVIRONMENT', choices: ['Release','Hotfix'],description: 'Please select the way of Deployment')]
                            def INPUT_PARAMS = input message: 'Approval for Release Deployment',parameters: [choice(choices: ['Release', 'Hotfix'], name: 'Environment')]

                             def approver = input id: 'Deploy', message: 'Deploy to QA?', submitter: 'admin', submitterParameter: 'deploy_approver'
                             echo "This deployment was approved by ${approver}"
                        }
                    }
                }
                stage("Started Deployment to QA") {
                     when { branch "release/sprint/*" }  
                    steps {
                        sh 'echo Started QA release'
                    }
                }
                stage('Approval to UAT') {
                    when {expression { params.choices == 'Release' } }
                    // no agent is used, so executors are not used up when waiting for approvals
                    agent none
                    steps {
                        script {
                            def approver = input id: 'Deploy', message: 'Deploy to UAT?', submitter: 'pavan.prabhu,admin', submitterParameter: 'deploy_approver'
                            echo "This deployment was approved by ${approver}"
                        }
                    }
                }
                stage("Started Deployment to UAT") {
                    when { branch "release/sprint/*" }  
                    steps {
                        sh 'echo Started UAT release'
                    }
                }
                stage('Approval to PROD') {
                    when { branch "release/sprint/*" }  
                    // no agent is used, so executors are not used up when waiting for approvals
                    agent none
                    steps {
                        script {
                            def approver = input id: 'Deploy', message: 'Deploy to PROD?', submitter: 'pavan.prabhu,admin', submitterParameter: 'deploy_approver'
                            echo "This deployment was approved by ${approver}"
                        }
                    }
                }
                stage("Started Deployment to PROD") {
                    steps {
                        sh 'echo Started PROD release'
                    }
                }
            }
        }
    }
}
