# What was the base
FROM ubuntu:latest

# What software is required
RUN apt update
RUN apt install -y git ssh

# What accounts need setup
RUN useradd -m -s /usr/bin/git-shell git
# this key problem
# BYOK model - bind mount host file authorized_keys -> /home/git/.ssh/authorized_keys
#   Pro - key is flexible
#   Con - back on the user to remember bind mount when they run container (use --mount)
# Dockerfile COPY
#   Pro - It's already there
#   Con - I bring it once , per build, otherwise I'm editing
# File manipulation
#   I have bash - therefore echo >> 
# RUN echo "public key goes here" >> /home/git/.ssh/authorized_keys
#  Pro - I can take advantage bash commands
#  Con - potential for Copy paste errors
WORKDIR /home/git/
COPY .ssh/banana.pub .ssh/authorized_keys

# Do we copy anything?

# Initialize a repo
RUN mkdir pattonsgirl
WORKDIR /home/git/pattonsgirl/
RUN git init --bare grapes.git
RUN chown -R git /home/git

# What do we want to happen on start
# Start the service - service ssh start 
#  Pro - the right command
#  Con - must shell in every time we start and run command anyway
#ENTRYPOINT ["/bin/bash"]
RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd
CMD ["/usr/sbin/sshd", "-D"]

