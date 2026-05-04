# ZDI-23-221: Parallels Desktop Toolgate Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-221
- **ZDI-CAN:** ZDI-CAN-18933
- **Date:** 2023-03-07
- **CVE:** CVE-2023-27326
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Alexandre Adamski of Impalabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-221/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user on the host system.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
