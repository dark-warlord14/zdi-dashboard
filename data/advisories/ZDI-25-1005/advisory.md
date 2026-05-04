# ZDI-25-1005: Apple macOS WindowServer Excessive Iteration Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1005
- **ZDI-CAN:** ZDI-CAN-27348
- **Date:** 2025-11-13
- **CVE:** CVE-2025-43401
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1005/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Apple macOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WindowServer component. The issue results from the lack of proper validation of user-supplied data, which can result in an excessively long loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125635

## Disclosure Timeline

- 2025-07-08 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated
