# ZDI-25-574: Siemens SINEC NMS reqToChangePassword Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-574
- **ZDI-CAN:** ZDI-CAN-26569
- **Date:** 2025-07-08
- **CVE:** CVE-2025-40736
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-574/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Siemens SINEC NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the reqToChangePassword method. The issue results from the lack of authentication prior to allowing access to password change functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-078892.html

## Disclosure Timeline

- 2025-04-10 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
