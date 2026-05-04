# ZDI-25-845: (Pwn2Own) Microsoft Windows win32kfull Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-845
- **ZDI-CAN:** ZDI-CAN-27174
- **Date:** 2025-08-14
- **CVE:** CVE-2025-53132
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** goodbyeselene
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-845/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53132

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-08-14 - Coordinated public release of advisory
- 2025-08-14 - Advisory Updated
