# ZDI-24-563: NETGEAR ProSAFE Network Management System UpLoadServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-563
- **ZDI-CAN:** ZDI-CAN-22724
- **Date:** 2024-06-04
- **CVE:** CVE-2024-5505
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-563/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability. The specific flaw exists within the UpLoadServlet class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000066192/Security-Advisory-for-Missing-Function-Level-Access-Control-on-the-NMS300-PSV-2024-0008

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-06-04 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
