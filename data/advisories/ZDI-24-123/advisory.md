# ZDI-24-123: X.Org Server DeviceFocusEvent Improper Validation of Array Index Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-123
- **ZDI-CAN:** ZDI-CAN-22664
- **Date:** 2024-02-09
- **CVE:** CVE-2023-6816
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-123/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of SetInputFocus requests. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2023-6816

## Disclosure Timeline

- 2023-12-08 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
