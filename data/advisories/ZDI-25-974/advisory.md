# ZDI-25-974: X.Org Server XkbRemoveResourceClient Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-974
- **ZDI-CAN:** ZDI-CAN-27545
- **Date:** 2025-10-29
- **CVE:** CVE-2025-62230
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-974/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of resource objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2025-October/003635.html

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2025-10-29 - Coordinated public release of advisory
- 2025-10-29 - Advisory Updated
