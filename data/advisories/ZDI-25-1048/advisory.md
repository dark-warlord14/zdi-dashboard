# ZDI-25-1048: Microsoft Windows win32kfull Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1048
- **ZDI-CAN:** ZDI-CAN-27760
- **Date:** 2025-12-09
- **CVE:** CVE-2025-62458
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1048/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull driver. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62458

## Disclosure Timeline

- 2025-08-07 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
