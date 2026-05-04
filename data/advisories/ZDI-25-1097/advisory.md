# ZDI-25-1097: Fortinet FortiSandbox name Parameter Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1097
- **ZDI-CAN:** ZDI-CAN-27309
- **Date:** 2025-12-16
- **CVE:** CVE-2025-53949
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiSandbox
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiSandbox. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the name parameter provided to the interface endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-25-479

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-12-16 - Coordinated public release of advisory
- 2025-12-16 - Advisory Updated
