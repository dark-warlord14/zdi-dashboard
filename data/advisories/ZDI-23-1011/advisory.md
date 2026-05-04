# ZDI-23-1011: (Pwn2Own) PTC KEPServerEX Variant Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1011
- **ZDI-CAN:** ZDI-CAN-20500
- **Date:** 2023-07-31
- **CVE:** CVE-2023-3825
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** PTC
- **Affected Products:** KEPServerEX
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1011/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of PTC KEPServerEX. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of variant types. By sending a crafted request, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

PTC has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-208-02

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-07-31 - Coordinated public release of advisory
