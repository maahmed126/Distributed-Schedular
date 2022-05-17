pipeline {

    agent any
    stages {

        stage('Develop Deployment') {
                when { branch "develop" }
                steps {
                        sh 'echo Started DEV release'
                    }
                }
        

        
        stage('Hotfix Deployment and Release Deployment') {
            parallel {
                stage("HotfixDeployment") {
                    agent {
                        label "HotfixDeployment"
                    }
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
             
        stage("ReleaseDeployment") {
            agent {
                label "ReleaseDeployment"
            }
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
}
