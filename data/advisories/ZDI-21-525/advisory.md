# ZDI-21-525: Trend Micro IM Security Weak Session Token Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-525
- **ZDI-CAN:** ZDI-CAN-12023
- **Date:** 2021-05-07
- **CVE:** CVE-2021-31520
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** IM Security
- **Credit:** Quentin Kaiser
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-525/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro IM Security. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web console, which listens on TCP port 16373 by default. The issue results from the use of guessable session tokens. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000286439

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-05-07 - Coordinated public release of advisory
