# ZDI-21-660: Adobe RoboHelp Server folderId Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-660
- **ZDI-CAN:** ZDI-CAN-13088
- **Date:** 2021-06-10
- **CVE:** CVE-2021-28588
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-660/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe RoboHelp Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the RoboHelp server. When parsing the folderId parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb21-44.html

## Disclosure Timeline

- 2021-04-02 - Vulnerability reported to vendor
- 2021-06-10 - Coordinated public release of advisory
