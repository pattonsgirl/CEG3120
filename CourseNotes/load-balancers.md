## Web Servers 101

- DNS to IP, packet sent
    - if no DNS, can use `/etc/hosts` to do old-school IP to hostname listings
- packet includes destination IP, port, and uses default protocol for port

## Proxies

Forward proxy:

Reverse proxy:

[OxyLabs - forward vs. reverse proxies](https://oxylabs.io/blog/reverse-proxy-vs-forward-proxy)

## Load Balancers

- Reverse proxy that distributes network or application traffic across a number of servers
- Concurrency of users and reliability of applications
- Sometimes called **Application Delivery Controllers** (ADC)

Terminology:
- Virtual server / proxy / ADC – endpoint presented to outside world
- Pool / cluster / farm – collection of services available on hosts
- Host(s) – server that will receive traffic from the ADC
  - Hosts include the definition of the application port and their IP
  - 172.16.1.10:80 is listening on port 80
    - Also known as the service (what is running)
  - Host can have multiple services available, thus detail in ports

Types of Load Balancers:
- Layer 4 (transport layer)
    - forward user traffic based on IP range and port 
    - i.e. if a request comes in for `http://yourdomain.com/anything`, the traffic will be forwarded to the backend that handles all the requests for `yourdomain.com` on port `80`
![DigitalOcean - L4 LB](https://assets.digitalocean.com/articles/HAProxy/layer_4_load_balancing.png)
- Layer 7 (application layer)
    - forward requests to different backend servers based on the content of the user’s request
    - i.e. if a request comes in for `http://yourdomain.com/blog`, the traffic will be forwarded to the set of backend servers defined to have content for `/blog` requests 
    - This mode of load balancing allows you to run multiple web application servers under the same domain and port
![DigitalOcean - L7 LB](https://assets.digitalocean.com/articles/HAProxy/layer_7_load_balancing.png)

Allocation Strategies / Algorithms:
- Round robin
    - Selects hosts in turns
- Weighted round robin
- Least connections
    - Assigns the next request to a less busy server(the server with the least number of active connections)
- Least response time
- source / ip-hash
    - select host for the next request based on the client’s IP address. 
    - This method allows for session persistence (tie a client to a particular application server).

Software for ADC:
- HAProxy
- [NGINX](https://www.tecmint.com/use-nginx-as-http-load-balancer-in-linux/)
- Commercial (paid) ADCs
    - AWS has [ELB (Elastic Load Balancer)](https://aws.amazon.com/elasticloadbalancing/)
    - [DigitalOcean - droplets as LBs](https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps)
- this also brings in conversations about auto-scaling

Configuring HAProxy:
- backend
- frontend
- global
- defaults

**Resources**
- [DigitalOcean - Intro to HAProxy and LB Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)

Health Tests:
- `ping hostname`
- `nmap -A -Pn hostname`
- `hi`
- `hurl`

