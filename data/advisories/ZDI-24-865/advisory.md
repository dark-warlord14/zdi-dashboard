# ZDI-24-865: Phoenix Contact CHARX SEC-3100 charx_pack_logs Improper Input Validation Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-865
- **ZDI-CAN:** ZDI-CAN-21407
- **Date:** 2024-06-21
- **CVE:** CVE-2024-25999
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Todd Manning
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-865/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Phoenix Contact CHARX SEC-3100 charging controllers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the charx_pack_logs script. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
