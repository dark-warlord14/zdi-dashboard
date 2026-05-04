# ZDI-20-877: Microsoft Windows PFB Font File Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-877
- **ZDI-CAN:** ZDI-CAN-10903
- **Date:** 2020-07-16
- **CVE:** CVE-2020-1436
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-877/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the parsing of fonts. Crafted data in a font can trigger a write past the end of a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-1436

## Disclosure Timeline

- 2020-05-07 - Vulnerability reported to vendor
- 2020-07-16 - Coordinated public release of advisory
