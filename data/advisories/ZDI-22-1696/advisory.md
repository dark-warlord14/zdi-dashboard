# ZDI-22-1696: X.Org Server ProcXIPassiveUngrabDevice Improper Validation of Array Index Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1696
- **ZDI-CAN:** ZDI-CAN-19381
- **Date:** 2022-12-28
- **CVE:** CVE-2022-46341
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1696/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ProcXIPassiveUngrabDevice requests. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2022-December/003302.html

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2022-12-28 - Coordinated public release of advisory
