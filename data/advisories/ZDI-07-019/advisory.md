# ZDI-07-019: BMC Patrol PerformAgent bgs_sdservice Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-019
- **ZDI-CAN:** ZDI-CAN-151
- **Date:** 2007-04-18
- **CVE:** CVE-2007-2136
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** BMC Software
- **Affected Products:** Patrol
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-019/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of BMC Patrol. User interaction is not required to exploit this vulnerability. The specific flaw exists due to improper parsing of XDR data sent to the bgs_sdservice.exe process listening by default on TCP port 10128. An attacker can influence a parameter to a memory copy operation and cause corruption of the stack and including SEH pointers. This can be leveraged to execute arbitrary code.

## Additional Details

[This issue] has been addressed, and a patch has been made available to our customers. A flash bulletin has been created describing the patch and will be sent to all affected customers in the next few days. BMC has a formal customer support mechanism in place to provide solutions to security issues brought to us by those who have legally licensed our software. In cases where security issues are brought to my attention by individuals/vendors who do not have legal access to our products, we will investigate their merit; however the issues will be addressed at our own discretion and according to our understanding of their severity. Finally, please note that in the future, I will only communicate resolutions and workarounds to licensed customers who are using our software legally. For a more meaningful dialogue around these issues and to be notified of any available patches, I urge all licensed customers to use BMC's support mechanism.

## Disclosure Timeline

- 2007-03-05 - Vulnerability reported to vendor
- 2007-04-18 - Coordinated public release of advisory
