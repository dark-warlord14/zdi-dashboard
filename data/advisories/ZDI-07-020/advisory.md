# ZDI-07-020: BMC Performance Manager SNMP Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-020
- **ZDI-CAN:** ZDI-CAN-153
- **Date:** 2007-04-18
- **CVE:** CVE-2007-1972
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** BMC Software
- **Affected Products:** Performance Manager for Servers
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-020/
## Vulnerability Details

These vulnerabilities allows attackers to execute arbitrary code on vulnerable installations of BMC Performance Manager. User interaction is not required to exploit this vulnerability. The specific flaw exists in the PatrolAgent.exe listening on TCP port 3181. The service allows remote attackers to modify configuration files without authentication. This can be exploited by an attacker by modifying parameters in SNMP communities definitions. By modifying the masterAgentName and masterAgentStartLine parameters, an attacker can execute arbitrary code.

## Additional Details

[This issue] has been found not to be a security vulnerability; when properly configured (as described for our customers in our documentation and in our online knowledge base) this attack is not possible. BMC has a formal customer support mechanism in place to provide solutions to security issues brought to us by those who have legally licensed our software. In cases where security issues are brought to my attention by individuals/vendors who do not have legal access to our products, we will investigate their merit; however the issues will be addressed at our own discretion and according to our understanding of their severity. Finally, please note that in the future, I will only communicate resolutions and workarounds to licensed customers who are using our software legally. For a more meaningful dialogue around these issues and to be notified of any available patches, I urge all licensed customers to use BMC's support mechanism.

## Disclosure Timeline

- 2007-03-05 - Vulnerability reported to vendor
- 2007-04-18 - Coordinated public release of advisory
