# Description
-This is a simple distributed web design infrastructure with two servers. Traffic and requests from clients being handled by a load balancer which directs traffic to the servers based on their current state and available resources to handle requests. Hence reducing the chances of network overload or web site downtime.

# Specifics About This Infrastructure
-For every additional element, why you are adding it?

-The additional elements here is the load balancer and an additional server with similar setup to the previous one. The laod balancer is added to help split traffic over two servers, as it requires at least two servers for this setup to work. The additional server is to add more resources to the infrastructure and reduce the chances of downtime.

What distribution algorithm your load balancer is configured with and how it works?

The HAProxy load balancer is configured with Round Robin configuration, where each server receives client's request in turns based on the configuration and weight of the server. The setup is very fair and easy to adjust as it is a dynamic algorithm. The server weights can be adjusted on the go.

Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?

This configuration uses the active-passive setup.

The Active-Active setup: The active-active setup is made up of at least two nodes, with each node running similar service(s) simultaneously. The purpose of this is to achieve load balancing across both nodes. The load balancer distributes traffic across all nodes, thus preventing a node form overload and sutthing down.

The Active-Passive setup is also similar, requiring at least two nodes operating similar service(s) but as the name implies, not all nodes are used simultaneously. While one node is active, the other node will be in passive or standby mode. Hence acting as a failover.

How a database Primary-Replica (Master-Slave) cluster works?
As the name applies, there will be two database in this setup, with one as the master, and the other as a slave to the master. The master receivss all of the queries, executes the queries and then logs the queries, which is then sent to the slave to execute and hence to keep the same data across all of the replication members.

What is the difference between the Primary node and the Replica node in regard to the application

The replica node is designed to be a mirror copy of the master node/configuration and have the current cluster state in real time so that if the master nodes become unavailable the cluster can fail over to the replica nodes automatically whenever they are needed.

# Issues With This Infrastructure
Where are SPOF?

In this infrastructure, the major point of failure is the database server which is a single replica server. Hence if the database is down, the web site is also going to experience downtime. Also there is a chance of data loss if the master database unsuccessfully transfer its log/data to the slave nodes before going offline or for maintenance.

Security issues (no firewall, no HTTPS)

All requests to and from the server are in plain text/format. No encryption and security. This design is prone to data theft and loss of data.

No monitoring

While this design has a load balancer to help spread out and balance the traffic/requests across the two servers, there is still an issue with monitoring, to know when the server's resources are being maxed out. Where there's no monitoring, there is still the risk of server overload and site downtime.