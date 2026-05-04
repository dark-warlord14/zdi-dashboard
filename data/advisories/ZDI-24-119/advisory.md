# ZDI-24-119: X.Org Server DisableDevice Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-119
- **ZDI-CAN:** ZDI-CAN-22840
- **Date:** 2024-02-09
- **CVE:** CVE-2024-21886
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-119/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DisableDevice function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/cve-2024-21886

## Disclosure Timeline

- 2023-12-20 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
