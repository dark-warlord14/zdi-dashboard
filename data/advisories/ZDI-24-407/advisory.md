# ZDI-24-407: X.Org Server ProcRenderAddGlyphs Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-407
- **ZDI-CAN:** ZDI-CAN-22880
- **Date:** 2024-04-26
- **CVE:** CVE-2024-31083
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-407/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ProcRenderAddGlyphs function. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2024-April/003497.html

## Disclosure Timeline

- 2024-01-12 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
