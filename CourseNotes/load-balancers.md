## Web Servers 101

- DNS to IP, packet sent
    - if no DNS, can use `/etc/hosts` to do old-school IP to hostname listings
- packet includes destination IP, port, and uses default protocol for port
- server is contacted at that port
    - if a service is running on that port
    - and if the service knows that protocol
- service running on server returns requested info

Web Content Services:
- Apache HTTP Server aka. apache2
    - [How to Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- NGINX
    - [How to Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)

Useful commands:
```bash
systemctl status/restart/start/stop servicename
nmap -A -Pn hostname/ip
curl hostname/ip
```

Web Server Error Codes:

- [Mozilla - HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [The Story of Response Code 418](https://www.berkeleysquares.co.uk/2021/06/html-response-code-418-why-youve-never-heard-of-it-and-never-will-again/) 
    - [The teapot lives on](https://www.google.com/teapot)

## Proxies

### Forward proxy:
- sits in front of a client and ensures that no origin server ever communicates directly with that specific client
    - You connect to forward proxy
    - Destination is contacted by forward proxy's IP, not yours
![Cloudflare - forward proxy flow](https://cf-assets.www.cloudflare.com/slt3lc6tev37/2MZmHGnCdYbQBIsZ4V11C6/25b48def8b56b63f7527d6ad65829676/forward_proxy_flow.png)

Reasons to use forward proxy:
- To avoid state or institutional browsing restrictions
- To block access to certain content
- To protect online identity
- To access content with restrictions based on geo-location

### Reverse proxy:
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
- SSL encryption (aka. [SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination/))
    - server decrypts / encrypts communications on behalf of host

[Cloudflare - reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)
[OxyLabs - forward vs. reverse proxies](https://oxylabs.io/blog/reverse-proxy-vs-forward-proxy)

### VPN (Virtual Private Network):

Can't mention forward proxies without comparing them to VPNs.

A VPN client on your computer establishes a secure tunnel with the VPN server, replacing your local ISP routing. 

VPN connections encrypt and secure all of your network traffic, not just the HTTP or SOCKS calls from your browser like a proxy server.

[Varonis - proxy vs VPN](https://www.varonis.com/blog/proxy-vs-vpn)


## Load Balancers

### What is it: 
- Reverse proxy that distributes network or application traffic across a number of servers
- Concurrency of users and reliability of applications
- Sometimes called **Application Delivery Controllers** (ADC)

### Terminology:
- Virtual server / proxy / ADC – endpoint presented to outside world
- Pool / cluster / farm – collection of services available on hosts
- Host(s) – server that will receive traffic from the ADC
  - Hosts include the definition of the application port and their IP
  - 172.16.1.10:80 is listening on port 80
    - Also known as the service (what is running)
  - Host can have multiple services available, thus detail in ports

### How Load Balancers Work:

1. The client attempts to connect with the service.
2. The ADC accepts the connection, and after deciding which host should receive the connection, changes the destination IP (and possibly port) to match the service of the selected host (note that the source IP of the client is not touched).
3. The host accepts the connection and responds back to the original source, the client, via its default route, the ADC.
4. The ADC intercepts the return packet from the host and now changes the source IP (and possible port) to match the virtual server IP and port, and forwards the packet back to the client.
5. The client receives the return packet, believing that it came from the virtual server, and continues the process.

[f5 - Load Balancing 101](f5.com/services/resources/white-papers/load-balancing-101-nuts-and-bolts)

### Types of Load Balancers:
- Layer 4 (transport layer)
    - forward user traffic based on IP range and port 
    - i.e. if a request comes in for `http://yourdomain.com/anything`, the traffic will be forwarded to the backend that handles all the requests for `yourdomain.com` on port `80`
![DigitalOcean - L4 LB](https://assets.digitalocean.com/articles/HAProxy/layer_4_load_balancing.png)
- Layer 7 (application layer)
    - forward requests to different backend servers based on the content of the user’s request
    - i.e. if a request comes in for `http://yourdomain.com/blog`, the traffic will be forwarded to the set of backend servers defined to have content for `/blog` requests 
    - This mode of load balancing allows you to run multiple web application servers under the same domain and port
![DigitalOcean - L7 LB](https://assets.digitalocean.com/articles/HAProxy/layer_7_load_balancing.png)

### Allocation Strategies / Algorithms:
- Round robin
    - Selects hosts in turns
- Weighted round robin
- Least connections
    - Assigns the next request to a less busy server(the server with the least number of active connections)
- Least response time
- source / ip-hash
    - select host for the next request based on the client’s IP address. 
    - This method allows for session persistence (tie a client to a particular application server).

### Software for ADC:
- HAProxy
- [NGINX](https://www.tecmint.com/use-nginx-as-http-load-balancer-in-linux/)
- Commercial (paid) ADCs
    - AWS has [ELB (Elastic Load Balancer)](https://aws.amazon.com/elasticloadbalancing/)
    - [DigitalOcean - droplets as LBs](https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps)
- this also brings in conversations about auto-scaling

### Configuring HAProxy:
- `global`
    - Settings define process-wide security and performance tunings that affect HAProxy at a low level
- `defaults`
    - Settings apply to all of the frontend and backend sections that come after it
- `backend`
    - defines a group of servers that will be load balanced and assigned to handle requests
    - You’ll add a label of your choice to each backend, such as web_servers. It’s generally, pretty straightforward and you won’t often need many settings here.
- `frontend`
    - defines the IP addresses and ports that clients can connect to
    - You may add as many frontend sections as needed for exposing various websites to the Internet. 
    - Each frontend keyword is followed by a label, such as www.mysite.com, to differentiate it from others.

**Resources**
- [HAProxy - The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [DigitalOcean - Intro to HAProxy and LB Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)

### Health Monitoring & Fault Tolerance:
- `ssh` and check things?
- `cron` job running a check report?
- [configure and view `haproxy` logs](https://www.haproxy.com/blog/introduction-to-haproxy-logging/)
- [`haproxy` `stats` page](https://www.haproxy.com/blog/exploring-the-haproxy-stats-page/)
    - check port bind is open on firewall (Security Groups)
    - `stats uri ` of `/haproxy?stats` or `/stats` needs to be configured in `frontend`
    - access with `EIP:port/uri`
- [managing hosts with `haproxy` via command line](https://serverfault.com/questions/249316/how-can-i-remove-balanced-node-from-haproxy-via-command-line)

Useful commands:
- `ping hostname`
- `nmap -A -Pn hostname`
- [`hey`](https://github.com/rakyll/hey)
- [`hurl`](https://github.com/Orange-OpenSource/hurl)

### Persistence

`source/ip hash` is an allocation strategy that reconnects you with the server you were communicating with.

How about remembering you logged on?

#### JSON Web Tokens

- [JWTs - JSON Web Tokens](https://www.youtube.com/watch?v=soGRyl9ztjI&ab_channel=JavaBrains)
- [Decode a JWT](https://jwt.io/)
- Playing with JWT
    - [realpython - tokens with flask](https://realpython.com/token-based-authentication-with-flask/)
    - [JSON vs OAuth](https://anil-pace.medium.com/json-web-tokens-vs-oauth-2-0-85dd0b32057d)
    - [JWT vs Cookies](https://dzone.com/articles/cookies-vs-tokens-the-definitive-guide)

#### OpenIDConnect

- [auth0 - id vs access token](https://auth0.com/blog/id-token-access-token-what-is-the-difference/)
- [openid - what is it?](https://openid.net/connect/)
- [auth0 - using openid connect protocol](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol)

### Dashboards

- [Grafana](https://grafana.com/grafana/dashboards/12693-haproxy-2-full/)
- [Datadogs](https://www.datadoghq.com/dashboards/haproxy-dashboard/)

### Case Studies

#### repl.it

- https://blog.replit.com/geo-part-1-controlplane
- https://blog.replit.com/geo-part-2-loadbalancing

#### Netflix

- https://netflixtechblog.com/netflix-edge-load-balancing-695308b5548c
- https://netflixtechblog.com/netflix-shares-cloud-load-balancing-and-failover-tool-eureka-c10647ef95e5

### Vulnerabilities

- [HTTP Request Smuggling in HAProxy](https://portswigger.net/daily-swig/amp/http-request-smuggling-bug-patched-in-haproxy)
    - [CVE Notice](https://www.mail-archive.com/haproxy@formilux.org/msg43229.html)
