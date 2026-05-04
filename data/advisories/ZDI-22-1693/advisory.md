# ZDI-22-1693: Microsoft Windows PlgBlt Untrusted Pointer Dereference Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1693
- **ZDI-CAN:** ZDI-CAN-18523
- **Date:** 2022-12-28
- **CVE:** CVE-2022-41121
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1693/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the PlgBlt graphics primitive. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41121

## Disclosure Timeline

- 2022-09-08 - Vulnerability reported to vendor
- 2022-12-28 - Coordinated public release of advisory
