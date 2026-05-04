# ZDI-20-1420: X.Org Server XkbSetMap Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1420
- **ZDI-CAN:** ZDI-CAN-11572
- **Date:** 2020-12-09
- **CVE:** CVE-2020-14360
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1420/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XkbSetMap requests. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2020-December/003066.html

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory
