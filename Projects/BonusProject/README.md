# Bonus Option

## Bonus 1 - Return of the Load Balancer

You now have a containerized web application.  Revisit your load balancing project, and have your hosts run your containerized web application instead of your manually configured web services.  Your objectives are as follows:
1. Revise the CloudFormation template to install only software needed on each instance
    - This could be done last after you have fidgeted with building things down and know what software is need and on which instance
    - Don't forget we deleted the NAT Gateway and released the EIP associated with it if you are going to start by reusing your existing load balancing setup
2. Determine a method of updating all hosts when a new image is pushed to your DockerHub repository
3. Implement your method of updating all hosts when a new image is pushed to your DockerHub repository

Advanced tools that could be useful.  I would actually avoid these, but they are allowed solutions for the adventurous:
- Docker Compose
- Kubernetes

### Deliverables:

Utilize the repository you have been using for Projects 4 & 5.  Create a folder named "BONUS".

- All scripts you created, organized with what needs to go on hosts versus on the proxy
- Updated CF template
- A diagram to explain the flow of things
- Documentation sufficient to explain your implementation, how it works, and what steps need to be done to recreate it.  
    - You should reflect on project documentation requirements up to this point when determining what I mean by "sufficient".  
    - Insufficient documentation will not get credit - this can include poor / illegible documentation formatting.

## Submission

Submit the link to your repository `BONUS` folder to the Bonus Dropbox on Pilot.