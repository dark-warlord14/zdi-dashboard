# ZDI-21-287: Microsoft Windows win32kfull bStretch NULL Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-287
- **ZDI-CAN:** ZDI-CAN-12672
- **Date:** 2021-03-15
- **CVE:** CVE-2021-27077
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-287/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull.sys driver. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-27077

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
