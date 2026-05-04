# ZDI-24-495: (Pwn2Own) Microsoft Windows CLFS Integer Underflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-495
- **ZDI-CAN:** ZDI-CAN-23790
- **Date:** 2024-05-22
- **CVE:** CVE-2024-30037
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** HackInside (Yongil Lee, Ingyu Tae, Louis Hur)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-495/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Common Log File System (CLFS). The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30037

## Disclosure Timeline

- 2024-05-21 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
