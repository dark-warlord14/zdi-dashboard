# ZDI-25-139: X.Org Server CreatePointerBarrierClient Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-139
- **ZDI-CAN:** ZDI-CAN-25740
- **Date:** 2025-03-13
- **CVE:** CVE-2025-26598
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-139/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of disabled pointer devices. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2025-February/003584.html

## Disclosure Timeline

- 2024-12-11 - Vulnerability reported to vendor
- 2025-03-13 - Coordinated public release of advisory
- 2025-03-13 - Advisory Updated
