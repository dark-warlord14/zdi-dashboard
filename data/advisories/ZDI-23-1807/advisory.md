# ZDI-23-1807: X.Org Server Damage Object Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1807
- **ZDI-CAN:** ZDI-CAN-21213
- **Date:** 2023-12-19
- **CVE:** CVE-2023-5574
- **CVSS:** 7.4
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Sri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1807/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Damage objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2023-October/003430.html

## Disclosure Timeline

- 2023-06-13 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
