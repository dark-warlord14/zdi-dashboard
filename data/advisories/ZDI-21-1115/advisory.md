# ZDI-21-1115: Trend Micro ServerProtect Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1115
- **ZDI-CAN:** ZDI-CAN-12771
- **Date:** 2021-09-26
- **CVE:** CVE-2021-36745
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Yuto Maeda from Cyber Defense Institute, Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1115/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro ServerProtect. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ServerProtect console. The issue results from the lack of proper validation prior to authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289038

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-09-26 - Coordinated public release of advisory
