# ZDI-21-113: Trend Micro OfficeScan Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-113
- **ZDI-CAN:** ZDI-CAN-11737
- **Date:** 2021-01-29
- **CVE:** CVE-2021-25240
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Elias Martinez (FileNotFound)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-113/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro OfficeScan. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web console, which listens on TCP port 4343 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information from the application.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000284202

## Disclosure Timeline

- 2020-08-26 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
