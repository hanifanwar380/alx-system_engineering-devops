# Description
This design introduces security and monitoring components to the setup. This helps to have a more secure setup and gives real time feedback to the admin on the health status of the design. With this monitoring in place, the downtime of the site can be greatly reduced if not completely eliminated.

Specifics About This Infrastructure
For every additional element, why you are adding it.

The additional equipment/resources added are to improve the performance of the infrastructure and most importantly the security this setup. The HTTP connections are now encrypted over SSL, the firewalls prevent unauthorized access and the monitoring tool helps to have a detailed overview on the performace of the system.

What are firewalls for?

Firewalls are basically protecting the network(server, web server, application server) from unauthorized access. It acts as an intermediary between the internal network and the external network, blocking requests and traffic that don't meet the configured criteria.

Why is the traffic served over HTTPS?

The SSL certificate is for encrypting the traffic between the web servers and the external network(the client). This prevents a form of hacking attack called the Man in the middle attacks as well as network sniffers. The SSL certificate ensures the privacy of data and integrity of data.

What monitoring is used for?

Monitoring clients are used to monitor the servers and external network/incoming traffic and requests. hey analyse the performance and operations of the servers, measure the overall health, and alert the administrators if the servers are not performing as expected.

How the monitoring tool is collecting data?

The monitoring tools observe the servers and provides important metrics about the servers' operations to the admin. It automatically tests the accessibility of the servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues.

Explain what to do if you want to monitor your web server QPS

# Issues With This Infrastructure
Why terminating SSL at the load balancer level is an issue?

Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted. Network sniffers can take advantage of this.

Why having only one MySQL server capable of accepting writes is an issue?

Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.

Why having servers with all the same components (database, web server and application server) might be a problem?

Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable.