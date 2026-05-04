# ZDI-21-1305: Adobe RoboHelp Server Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1305
- **ZDI-CAN:** ZDI-CAN-14223
- **Date:** 2021-11-11
- **CVE:** CVE-2021-42727
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Dusan Stevanovic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1305/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe RoboHelp Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the RoboHelp server. When parsing the fileName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb21-87.html

## Disclosure Timeline

- 2021-06-24 - Vulnerability reported to vendor
- 2021-11-11 - Coordinated public release of advisory
