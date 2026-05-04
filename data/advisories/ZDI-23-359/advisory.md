# ZDI-23-359: X.Org Server Overlay Window Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-359
- **ZDI-CAN:** ZDI-CAN-19866
- **Date:** 2023-03-31
- **CVE:** CVE-2023-1393
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-359/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of overlay windows. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/xorg/xserver/-/commit/26ef545b3

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
