# ZDI-25-1094: Fortinet FortiWeb ApacheCookie_parse Improper Verification of Cryptographic Signature Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1094
- **ZDI-CAN:** ZDI-CAN-28211
- **Date:** 2025-12-16
- **CVE:** CVE-2025-64447
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1094/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Fortinet FortiWeb. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ApacheCookie_parse method. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-25-945

## Disclosure Timeline

- 2025-10-10 - Vulnerability reported to vendor
- 2025-12-16 - Coordinated public release of advisory
- 2025-12-16 - Advisory Updated
