# ZDI-26-298: Siemens SINEC NMS Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-298
- **ZDI-CAN:** ZDI-CAN-27564
- **Date:** 2026-04-23
- **CVE:** CVE-2026-24032
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-298/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Siemens SINEC NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd authentication handler. The issue results from incorrect implementation of an authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-801704.html

## Disclosure Timeline

- 2025-12-24 - Vulnerability reported to vendor
- 2026-04-23 - Coordinated public release of advisory
- 2026-04-23 - Advisory Updated
