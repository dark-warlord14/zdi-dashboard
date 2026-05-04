# ZDI-17-446: Cisco Prime Collaboration Provisioning licensestatus Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-446
- **ZDI-CAN:** ZDI-CAN-4467
- **Date:** 2017-06-26
- **CVE:** CVE-2017-6635
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Prime Collaboration Provisioning
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-446/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Cisco Prime Collaboration Provisioning. Authentication is not required to exploit this vulnerability. The specific flaw exists within the licensestatus.jsp page, which listens on TCP port 443 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any file accessible to the root user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170517-pcp3

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-06-26 - Coordinated public release of advisory
