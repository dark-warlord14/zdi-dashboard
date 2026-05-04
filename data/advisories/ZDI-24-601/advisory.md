# ZDI-24-601: (Pwn2Own) Microsoft Windows cldflt Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-601
- **ZDI-CAN:** ZDI-CAN-23845
- **Date:** 2024-06-12
- **CVE:** CVE-2024-30085
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Gwangun Jung(@pr0ln) and Junoh Lee(@bbbig12) at Theori(@theori_io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-601/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cldflt kernel driver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30085

## Disclosure Timeline

- 2024-04-03 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
