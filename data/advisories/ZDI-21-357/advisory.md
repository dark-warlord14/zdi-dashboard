# ZDI-21-357: NETGEAR ProSAFE Network Management System MFileUploadController Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-357
- **ZDI-CAN:** ZDI-CAN-12124
- **Date:** 2021-03-26
- **CVE:** CVE-2021-27274
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-357/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MFileUploadController class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062688/Security-Advisory-for-Pre-Authentication-Command-Injection-on-NMS300-PSV-2020-0560

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-03-26 - Coordinated public release of advisory
