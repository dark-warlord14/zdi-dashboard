# ZDI-26-266: Fortinet FortiWeb cat_cgi_paths Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-266
- **ZDI-CAN:** ZDI-CAN-28661
- **Date:** 2026-04-15
- **CVE:** CVE-2026-40688
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-266/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of HTTP requests. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-26-127

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
