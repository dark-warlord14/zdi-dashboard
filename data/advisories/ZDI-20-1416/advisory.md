# ZDI-20-1416: X.Org Server XkbSetNames Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1416
- **ZDI-CAN:** ZDI-CAN-11428
- **Date:** 2020-12-09
- **CVE:** CVE-2020-14345
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1416/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XkbSetNames requests. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2020-August/003058.html

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory
