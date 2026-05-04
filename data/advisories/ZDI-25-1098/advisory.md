# ZDI-25-1098: Fortinet FortiSandbox hcproxy Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1098
- **ZDI-CAN:** ZDI-CAN-27306
- **Date:** 2025-12-16
- **CVE:** CVE-2025-54353
- **CVSS:** 5.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiSandbox
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiSandbox. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the handling of HA cluster paths. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to interact with the application in the context of a target user.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-25-477

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-12-16 - Coordinated public release of advisory
- 2025-12-16 - Advisory Updated
