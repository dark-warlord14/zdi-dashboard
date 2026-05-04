# ZDI-23-1652: Adobe RoboHelp Server OnPublishFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1652
- **ZDI-CAN:** ZDI-CAN-21307
- **Date:** 2023-11-15
- **CVE:** CVE-2023-22273
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1652/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe RoboHelp Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the OnPublishFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb23-53.html

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
