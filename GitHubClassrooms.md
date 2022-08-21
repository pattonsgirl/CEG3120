# Guide to GitHub Classrooms

## Pre-Reqs:

- Have a GitHub account
  - [Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Have access to a terminal
  - [Environment Setup](EnvironmentSetup.md)

## Instructions

The Pilot page for this course, go to Content, then Labs.  Here there is a link labeled: "Create GitHub Classroom repo"  
Click the link when you are ready, then follow the instruction in [Setup](#Setup)

- [Setup](#Setup)
- [How to use](#How-to-use)

### Setup

- After click the "Create GitHub Classroom repo" link, you will be taken to github to finish creating your repo to use in this course
1. Select your wright.edu email address from the list shown.
  - If you misclick, email me so we can fix it
2. Select `OK` on the popup to confirm you selected the correct email address.
  ![Accept Assignment](Images/github-classrooms-acceptassignment.png)
3. Select `Accept this assignment`
4. After a minute, refresh the next page. You'll see something similar to:
  ![You're ready to go!](Images/github-classrooms-success.png)
4. Click the lower link / link that looks similar to: `https://github.com/WSU-kduncan/ceg2350-your_GitHub_username`. 
  - The top link sometimes presents an "error" but things are actually fine.
5. It may be convenient to bookmark this link for easy access down the road.

### How to use

- The repositories created in this course are **private**. The only people with access are you, me, and the TAs for this course.
- Your answers to the labs are generally going to go in a `README.md` file in a folder corresponding to the lab number. Each lab may work a little differently and have you add additional files and folders.
1. [Generate a new SSH key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) with the command:
  - `ssh-keygen -t ed25519 -C "your_email@example.com"`
  - Hit enter to skip any additional prompts
  - Pay attention to where the key pair was saved by default
  - **NOTE** You need to create a key pair on each system you want to use.
    - AWS Ubuntu system = 1 key pair
    - Your system = 1 key pair
    - A system at wright state = 1 key pair
2. Open the folder where the key pair was saved.  Look for the file that ends with `.pub`
3. Open the file, and copy its contents
4. [Add your public key to GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
  - Go to "Settings" - "SSH and GPG keys", then select "Add new key"
  - Give your key a useful name that ids which computer it belongs to
  - Paste the contents of the `.pub` file in the box
5. To `clone` the repository:
  - Click the green `Code` button
  - Select `SSH` for SSH key authentication
  - In a terminal use `git clone` followed by the corresponding URL to clone your repository
