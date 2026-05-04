# ZDI-23-920: NETGEAR ProSAFE Network Management System MyHandlerInterceptor Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-920
- **ZDI-CAN:** ZDI-CAN-19718
- **Date:** 2023-07-13
- **CVE:** CVE-2023-38096
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-920/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of NETGEAR ProSAFE Network Management System. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MyHandlerInterceptor class. The issue results from improper implementation of the authentication mechanism. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065707/Security-Advisory-for-Multiple-Vulnerabilities-on-the-ProSAFE-Network-Management-System-PSV-2023-0024-PSV-2023-0025

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-07-13 - Coordinated public release of advisory
