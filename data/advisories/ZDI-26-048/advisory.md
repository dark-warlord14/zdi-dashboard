# ZDI-26-048: Fortinet FortiSandbox fortisandbox Server-Side Request Forgery Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-048
- **ZDI-CAN:** ZDI-CAN-27307
- **Date:** 2026-01-28
- **CVE:** CVE-2025-67685
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiSandbox
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-048/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fortinet FortiSandbox. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of web sockets. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-25-783

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2026-01-28 - Coordinated public release of advisory
- 2026-01-28 - Advisory Updated
