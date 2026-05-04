# ZDI-26-172: Unraid Authentication Request Path Traversal Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-172
- **ZDI-CAN:** ZDI-CAN-28912
- **Date:** 2026-03-09
- **CVE:** CVE-2026-3839
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Unraid
- **Affected Products:** Unraid
- **Credit:** Nicolas Chatelain (Nicocha30)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-172/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Unraid. Authentication is not required to exploit this vulnerability. The specific flaw exists within the auth-request.php file. The issue results from the lack of proper validation of a user-supplied path prior to using it in authentications. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 7.2.4.

## Disclosure Timeline

- 2026-02-17 - Vulnerability reported to vendor
- 2026-03-09 - Coordinated public release of advisory
- 2026-03-09 - Advisory Updated
