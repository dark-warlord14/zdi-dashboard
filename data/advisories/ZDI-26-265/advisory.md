# ZDI-26-265: Fortinet FortiWeb cgi_buf_alloc Integer Overflow Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-265
- **ZDI-CAN:** ZDI-CAN-28660
- **Date:** 2026-04-15
- **CVE:** CVE-2026-39811
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-265/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of HTTP requests. Crafted requests can force the server into an infinite loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-26-108

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
