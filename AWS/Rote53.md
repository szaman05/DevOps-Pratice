# Route53:

* Only AWS service provide 100% SLA.
* CNAME can't be created example.com but can create www.example.com
* Alias is Route53 unique feature helps to redirect traffic to AWS internal resources without CNAME. EC2 and S3 DNS cannot be used here but S3 Website, ALM, Cloud Front and few others service are compatible for Alias. Positive part is no cost assosicated with this.
* Route53 Does not route traffic through it becuase its not a Router/ Load Balancer. It just a DNS with advanced features. So it just returns DNS query to clients.
