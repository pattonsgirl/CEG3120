## Web Servers 101

- DNS to IP, packet sent
    - if no DNS, can use `/etc/hosts` to do old-school IP to hostname listings
- packet includes destination IP, port, and uses default protocol for port
- server is contacted at that port
    - if a service is running on that port
    - and if the service knows that protocol
- service running on server returns requested info

## Proxies

Forward proxy:
- sits in front of a client and ensures that no origin server ever communicates directly with that specific client
    - You connect to forward proxy
    - Destination is contacted by forward proxy's IP, not yours
![Cloudflare - forward proxy flow](https://cf-assets.www.cloudflare.com/slt3lc6tev37/2MZmHGnCdYbQBIsZ4V11C6/25b48def8b56b63f7527d6ad65829676/forward_proxy_flow.png)

Reasons to use forward proxy:
- To avoid state or institutional browsing restrictions
- To block access to certain content
- To protect online identity
- To access content with restrictions based on geo-location

Reverse proxy:
- sits in front of an origin server and ensures that no client ever communicates directly with that origin server
    - You connect to destination
    - destination is a server sitting in front of (usually) web servers that have content
![Cloudflare - reverse proxy flow](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3msJRtqxDysQslvrKvEf8x/f7f54c9a2cad3e4586f58e8e0e305389/reverse_proxy_flow.png)

Reasons to implement reverse proxy:
- Load balancing
- Global Server Load Balancing 
    - server determines closest destination
- Protection from attacks
- Caching content
- SSL encryption
    - server decrypts / encrypts communications on behalf of host

[Cloudflare - reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)
[OxyLabs - forward vs. reverse proxies](https://oxylabs.io/blog/reverse-proxy-vs-forward-proxy)

VPN (Virtual Private Network):

Can't mention forward proxies without comparing them to VPNs.

A VPN client on your computer establishes a secure tunnel with the VPN server, replacing your local ISP routing. 

VPN connections encrypt and secure all of your network traffic, not just the HTTP or SOCKS calls from your browser like a proxy server.

[Varonis - proxy vs VPN](https://www.varonis.com/blog/proxy-vs-vpn)


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

How Load Balancers Work:

1. The client attempts to connect with the service.
2. The ADC accepts the connection, and after deciding which host should receive the connection, changes the destination IP (and possibly port) to match the service of the selected host (note that the source IP of the client is not touched).
3. The host accepts the connection and responds back to the original source, the client, via its default route, the ADC.
4. The ADC intercepts the return packet from the host and now changes the source IP (and possible port) to match the virtual server IP and port, and forwards the packet back to the client.
5. The client receives the return packet, believing that it came from the virtual server, and continues the process.

[f5 - Load Balancing 101](f5.com/services/resources/white-papers/load-balancing-101-nuts-and-bolts)

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

