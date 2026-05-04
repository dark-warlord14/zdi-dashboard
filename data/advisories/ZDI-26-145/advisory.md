# ZDI-26-145: Trend Micro Apex Central Scheduled Update Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-145
- **ZDI-CAN:** ZDI-CAN-26598
- **Date:** 2026-03-03
- **CVE:** CVE-2025-71206
- **CVSS:** 4.4
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:C/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Abdessamad Lahlali of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-145/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of URLs in the Scheduled Update feature. By providing a crafted URL, an attacker can cause the server to make a request to an incorrect URL. An attacker may be able to leverage this vulnerability to gain improper access to network resources.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0022071

## Disclosure Timeline

- 2025-03-04 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
