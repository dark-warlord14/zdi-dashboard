# ZDI-20-1083: Trend Micro Vulnerability Protection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1083
- **ZDI-CAN:** ZDI-CAN-11431
- **Date:** 2020-08-27
- **CVE:** CVE-2020-15605
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Vulnerability Protection
- **Credit:** Partick Hussey - Longwall Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1083/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro Vulnerability Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Vulnerability Protection console. The issue results from the lack of proper validation prior to authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000252039

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-08-27 - Coordinated public release of advisory
