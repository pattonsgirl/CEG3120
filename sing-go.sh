export VERSION=1.11 OS=linux ARCH=amd64 && \
wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
rm go$VERSION.$OS-$ARCH.tar.gz && \
echo 'export GOPATH=${HOME}/go' >> /home/ubuntu/.bashrc && \
echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> /home/ubuntu/.bashrc && \
source /home/ubuntu/.bashrc && \
go get -d github.com/sylabs/singularity
