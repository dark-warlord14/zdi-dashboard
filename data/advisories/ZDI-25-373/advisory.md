# ZDI-25-373: Trend Micro Endpoint Encryption DbAppDomain Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-373
- **ZDI-CAN:** ZDI-CAN-25519
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49216
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Endpoint Encryption
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-373/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro Endpoint Encryption. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DbAppDomain service. The issue results from an improper implementation of an authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019928

## Disclosure Timeline

- 2024-10-11 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
