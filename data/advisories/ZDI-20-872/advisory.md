# ZDI-20-872: (Pwn2Own) Microsoft Windows DirectComposition SetBufferProperty Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-872
- **ZDI-CAN:** ZDI-CAN-10779
- **Date:** 2020-07-16
- **CVE:** CVE-2020-1381
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** fluorescence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-872/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the DirectComposition SetBufferProperty function in the kernel. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-1381

## Disclosure Timeline

- 2020-03-26 - Vulnerability reported to vendor
- 2020-07-16 - Coordinated public release of advisory
