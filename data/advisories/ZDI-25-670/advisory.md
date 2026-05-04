# ZDI-25-670: Samsung MagicINFO 9 Server PremiumClientService Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-670
- **ZDI-CAN:** ZDI-CAN-25839
- **Date:** 2025-07-28
- **CVE:** CVE-2025-54454
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-670/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Samsung MagicINFO 9 Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PremiumClientService class. The issue results from a hard-coded cryptographic key. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2025-03-25 - Vulnerability reported to vendor
- 2025-07-28 - Coordinated public release of advisory
- 2025-07-28 - Advisory Updated
