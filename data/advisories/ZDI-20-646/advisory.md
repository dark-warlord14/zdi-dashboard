# ZDI-20-646: (Pwn2Own) Microsoft Windows DirectComposition SetReferenceArrayProperty Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-646
- **ZDI-CAN:** ZDI-CAN-10785
- **Date:** 2020-05-12
- **CVE:** CVE-2020-1135
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-646/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the DirectComposition SetReferenceArrayProperty function in the kernel. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1135

## Disclosure Timeline

- 2020-04-28 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
