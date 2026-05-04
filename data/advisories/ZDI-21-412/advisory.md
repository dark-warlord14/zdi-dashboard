# ZDI-21-412: Parallels Desktop Toolgate Directory Traversal Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-412
- **ZDI-CAN:** ZDI-CAN-12130
- **Date:** 2021-04-15
- **CVE:** CVE-2021-27278
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ezrak1e and Alisa Esage (Pwn2Own)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-412/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the current user on the host system.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
