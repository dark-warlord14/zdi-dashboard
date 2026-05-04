# ZDI-19-966: Microsoft Windows vResetSurfacePalette Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-966
- **ZDI-CAN:** ZDI-CAN-9359
- **Date:** 2019-11-11
- **CVE:** CVE-2019-1362
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-966/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the vResetSurfacePalette function in win32k.sys. The issue results from the lack of proper validation of user-supplied data, which can result in a write outside the bounds of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1362

## Disclosure Timeline

- 2019-09-04 - Vulnerability reported to vendor
- 2019-11-11 - Coordinated public release of advisory
