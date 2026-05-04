# ZDI-24-010: X.Org Server DeepCopyPointerClasses Out-Of-Bounds Access Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-010
- **ZDI-CAN:** ZDI-CAN-22413
- **Date:** 2024-01-04
- **CVE:** CVE-2023-6377
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-010/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Button Action objects. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2023-December/003435.html

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-01-04 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
