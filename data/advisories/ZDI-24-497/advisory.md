# ZDI-24-497: NETGEAR ProSAFE Network Management System Tomcat Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-497
- **ZDI-CAN:** ZDI-CAN-22868
- **Date:** 2024-05-22
- **CVE:** CVE-2024-5246
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** 191bb9f9c7b3a89d5a586e15299e24417a4aca4d
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-497/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from the use of a vulnerable version of Apache Tomcat. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000066164/Security-Advisory-for-Multiple-Vulnerabilities-on-the-NMS300-PSV-2024-0003-PSV-2024-0004

## Disclosure Timeline

- 2024-01-11 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
