# ZDI-22-964: X.Org Server ProcXkbSetGeometry Out-Of-Bounds Access Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-964
- **ZDI-CAN:** ZDI-CAN-16062
- **Date:** 2022-07-12
- **CVE:** CVE-2022-2319
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-964/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ProcXkbSetGeometry requests. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/938/diffs?commit_id=6907b6ea2b4ce949cb07271f5b678d5966d9df42

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-07-12 - Coordinated public release of advisory
