pipeline {
    agent any
   
    environment {
        RELEASE = "${env.BRANCH_NAME == "develop" || env.BRANCH_NAME == "release/sprint/*"}"
        DEPLOY_TO = "${env.BRANCH_NAME == "release/sprint/*" ? "hotfix" : env.BRANCH_NAME == "develop" ? "staging" : ""}"
    }
    
    stages {

        stage('Develop Deployment') {
                when { branch "develop" }
                steps {
                        sh 'echo Started DEV release'
                    }
                }
        properties([parameters([choice(choices: ['Hotfix Deployment', 'Release Deployment'], description: 'Select Deployment to Build', name: 'stage')])])
        
        stage('Hotfix Deployment') {
              when { branch "release/sprint/*" }
            
              stages('Hotfix Deployment Flow') {
                
              stage("Started Deployment to QA") {
                    steps {
                        sh 'echo Started QA release'
                    }
                }
                
               stage('Approval to PROD') {
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
                            def approver = input id: 'Deploy', message: 'Deploy to QA?', submitter: 'pavan.prabhu,admin', submitterParameter: 'deploy_approver'
                            echo "This deployment was approved by ${approver}"
                        }
                    }
                }
                stage("Started Deployment to QA") {
                    steps {
                        sh 'echo Started QA release'
                    }
                }
                stage('Approval to UAT') {
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
                    steps {
                        sh 'echo Started UAT release'
                    }
                }
                stage('Approval to PROD') {
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
