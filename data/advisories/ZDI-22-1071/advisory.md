# ZDI-22-1071: (Pwn2Own) Microsoft Windows partmgr Improper Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1071
- **ZDI-CAN:** ZDI-CAN-17426
- **Date:** 2022-08-18
- **CVE:** CVE-2022-33670
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** vinhthp1712
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1071/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the partmgr.sys driver. The issue results from improper authorization logic when accessing SCSI file handles. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33670

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
