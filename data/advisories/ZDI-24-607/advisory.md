# ZDI-24-607: (Pwn2Own) Microsoft Windows mskssrv Driver Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-607
- **ZDI-CAN:** ZDI-CAN-23789
- **Date:** 2024-06-12
- **CVE:** CVE-2024-30089
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Valentina Palmiotti, IBM X-Force
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-607/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Microsoft Kernel Streaming Server driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30089

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
