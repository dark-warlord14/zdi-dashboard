# ZDI-23-885: (Pwn2Own) Microsoft Windows mskssrv Driver Untrusted Pointer Dereference Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-885
- **ZDI-CAN:** ZDI-CAN-20735
- **Date:** 2023-06-16
- **CVE:** CVE-2023-29360
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Thomas Imbert (@masthoon) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-885/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the mskssrv driver. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29360

## Disclosure Timeline

- 2023-04-05 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
