# Bonus Options

You may complete one or both of the below. See [Submission](#submission) for submission requirements.

## Bonus 1 - Return of the Load Balancer - 5% Extra Credit

You now have a containerized web application.  Revisit your load balancing project and determine and implement a way for your hosts in the pool to update their containers when Dockerhub receives a new `latest` tag of your web app image.

Have your hosts run and update to the `latest` version of your web application container from the image in your DockerHub repository based on a payload trigger.

### Deliverables:

Utilize the repository you have been using for Projects 4 & 5.  Create a folder named `BONUS` or add text addressing `BONUS` implementations to your `README-CD.md`.

- Documentation sufficient to explain your implementation, how it works, and what steps need to be done to recreate it.  
    - You should reflect on project documentation requirements up to this point when determining what I mean by "sufficient".  
    - Insufficient documentation will not get credit - this can include poor / illegible documentation formatting or overly AI created solutions.

## Bonus 2 - [Zhu Li, Do the Thing!](https://www.youtube.com/watch?v=mofRHlO1E_A&ab_channel=AntoineBandele) - 5% Extra Credit

You now have a containerized web application.  Revisit your load balancing project, and rebuild the CloudFormation Template to the requirements of this project to automate as much of the setup as possible.

1. The CloudFormation Template updates should consider
    - software requirements on each instance (proxy and hosts)
    - service files as needed on each instance (proxy and hosts)
    - download file dependencies (such as the hooks definition file and scripts) to correct directories
    - security requirements (proxy and hosts)
    - [WARNING] Don't forget the NAT Gateway can be mischievous to your funds if left on when not in use

### Deliverables:

Utilize the repository you have been using for Projects 4 & 5.  Create a folder named `BONUS`or add text addressing `BONUS` implementations to your `README-CD.md`.

- CF template
- A diagram to explain the flow of things
- Documentation sufficient to explain your implementation and how it works
    - You should reflect on project documentation requirements up to this point when determining what I mean by "sufficient".  

## Submission

In your Project 5 submission, make note of which `BONUS` implementation you attempted and how you addressed it (where to look in your repo / documentation).