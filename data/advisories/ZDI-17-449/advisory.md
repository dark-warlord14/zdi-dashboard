# ZDI-17-449: Cisco Prime Collaboration Provisioning Logs Directory Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-449
- **ZDI-CAN:** ZDI-CAN-4344
- **Date:** 2017-06-26
- **CVE:** CVE-2017-6636
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Prime Collaboration Provisioning
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-449/
## Vulnerability Details

This vulnerability allows disclose sensitive information on vulnerable installations of Cisco Prime Collaboration Provisioning. Authentication is not required to exploit this vulnerability. The specific flaw exists within the service that listens on TCP port 443 by default. Access to the /logs/cupm directory is unrestricted. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170517-pcp4

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-06-26 - Coordinated public release of advisory
