# ZDI-25-289: Rockwell Automation ThinManager ThinServer Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-289
- **ZDI-CAN:** ZDI-CAN-25872
- **Date:** 2025-05-13
- **CVE:** CVE-2025-3618
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** Nikolai Skliarenko of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-289/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Rockwell Automation ThinManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ThinServer component. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1727.html

## Disclosure Timeline

- 2024-12-11 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-13 - Advisory Updated
