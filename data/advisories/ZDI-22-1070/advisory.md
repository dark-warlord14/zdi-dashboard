# ZDI-22-1070: (Pwn2Own) Microsoft Windows vhdmp Driver Improper Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1070
- **ZDI-CAN:** ZDI-CAN-17429
- **Date:** 2022-08-18
- **CVE:** CVE-2022-35751
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Phan Thanh Duy (@PTDuy), Le Huu Quang Linh (@linhlhq) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1070/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the vhdmp.sys driver. The issue results from improper authorization logic when accessing VHD files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35751

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
