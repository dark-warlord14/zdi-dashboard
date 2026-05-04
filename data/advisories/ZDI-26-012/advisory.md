# ZDI-26-012: (0Day) ALGO 8180 IP Audio Alerter Web UI Direct Request Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-012
- **ZDI-CAN:** ZDI-CAN-28299
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0790
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** ALGO
- **Affected Products:** 8180 IP Audio Alerter
- **Credit:** Vera Mensa of Claroty Research - Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-012/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ALGO 8180 IP Audio Alerter devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web-based user interface. By navigating directly to a URL, a user can gain unauthorized access to data. An attacker can leverage this vulnerability to disclose information in the context of the device.

## Additional Details

10/24/25 – ZDI requested the vendor’s PSIRT contacts via email 10/28/25 – the vendor asked for the affected version number 10/28/25 – ZDI provided the affected product version 10/30/25 – ZDI asked for updates 10/31/25 – the vendor provided their contacts 10/31/25 – ZDI submitted the report to the vendor 12/10/25 – ZDI asked for updates 12/17/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-11-05 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
