# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install Docker
USER root

# Install Docker using official script (compatible with Debian 12)
RUN apt-get update -y && \
    apt-get install -y curl && \
    curl -fsSL https://get.docker.com | sh && \
    apt-get clean

# Add Jenkins user to Docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Prepare Docker directory for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to Jenkins user
USER jenkins
