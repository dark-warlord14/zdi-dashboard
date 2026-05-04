# ZDI-25-238: Trend Micro Apex Central Query Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-238
- **ZDI-CAN:** ZDI-CAN-25524
- **Date:** 2025-04-09
- **CVE:** CVE-2025-30680
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Abdessamad Lahlali and Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-238/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the Query method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019355

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
