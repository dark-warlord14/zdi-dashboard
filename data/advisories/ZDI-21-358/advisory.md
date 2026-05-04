# ZDI-21-358: NETGEAR ProSAFE Network Management System ConfigFileController realName Directory Traversal Information Disclosure and Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-358
- **ZDI-CAN:** ZDI-CAN-12125
- **Date:** 2021-03-26
- **CVE:** CVE-2021-27275
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-358/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information and delete arbitrary files on affected installations of NETGEAR ProSAFE Network Management System. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ConfigFileController class. When parsing the realName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information or to create a denial-of-service condition on the system.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062687/Security-Advisory-for-Denial-of-Service-on-NMS300-PSV-2020-0561

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-03-26 - Coordinated public release of advisory
