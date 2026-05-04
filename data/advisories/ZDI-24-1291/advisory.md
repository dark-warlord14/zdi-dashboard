# ZDI-24-1291: Microsoft Windows Device Context Improper Release Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1291
- **ZDI-CAN:** ZDI-CAN-24091
- **Date:** 2024-09-26
- **CVE:** CVE-2024-38249
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1291/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull driver. The issue results from incorrect handling of a device context at the time of its release. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38249

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated
