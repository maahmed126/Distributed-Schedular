pipeline {
    agent any

    environment {
       RELEASE = "${env.BRANCH_NAME == "release/sprint/" || env.BRANCH_NAME == "main"}"
        DEPLOY_TO = "${env.BRANCH_NAME == "release/sprint/" ? "release" : env.BRANCH_NAME == "main" ? "production" : ""}"
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
                            def INPUT_PARAMS = input message: 'Approval for Release Deployment', ok: 'Next', parameters: [choice(name: 'ENVIRONMENT', choices: ['Release','Hotfix'].join('\n'),description: 'Please select the way of Deployment')]
                             def approver = input id: 'Deploy', message: 'Deploy to QA?', submitter: 'admin', submitterParameter: 'deploy_approver'
                             echo "This deployment was approved by ${approver}"
                        }
                    }
                }
                stage("Started Deployment to QA") {
                    when { ${ENVIRONMENT} == "Release" } 
                    steps {
                        sh 'echo Started QA release'
                    }
                }
                stage('Approval to UAT') {
                    when { ${ENVIRONMENT} == "Release" }
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
                    when { ${ENVIRONMENT} == "Release"  }
                    steps {
                        sh 'echo Started UAT release'
                    }
                }
                stage('Approval to PROD') {
                    when { ${ENVIRONMENT} == "Release" } }
                    // no agent is used, so executors are not used up when waiting for approvals
                    agent none
                    steps {
                        script {
                            def approver = input id: 'Deploy', message: 'Deploy to PROD?', submitter: 'admin', submitterParameter: 'deploy_approver'
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
