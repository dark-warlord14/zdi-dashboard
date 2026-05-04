# ZDI-21-1000: (Pwn2Own) Parallels Desktop WinAppHelper Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1000
- **ZDI-CAN:** ZDI-CAN-13543
- **Date:** 2021-08-25
- **CVE:** CVE-2021-34864
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Sunjoo Park (grigoritchy)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1000/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the WinAppHelper component. The issue results from the lack of proper access control. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Fixed in version 17

## Disclosure Timeline

- 2021-04-11 - Vulnerability reported to vendor
- 2021-08-25 - Coordinated public release of advisory
- 2021-08-26 - Advisory Updated
