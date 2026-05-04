# ZDI-25-614: Hewlett Packard Enterprise AutoPass License Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-614
- **ZDI-CAN:** ZDI-CAN-25791
- **Date:** 2025-07-17
- **CVE:** CVE-2025-37107
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-614/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Hewlett Packard Enterprise AutoPass License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 5814 by default. The issue results from making an authorization decision based on a non-canonical URL. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://myenterpriselicense.hpe.com/cwp-ui/product-details/APLS/9.18/sw_free

## Disclosure Timeline

- 2024-12-11 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
