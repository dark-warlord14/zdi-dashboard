# ZDI-26-295: (0Day) PublicCMS getXml Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-295
- **ZDI-CAN:** ZDI-CAN-23734
- **Date:** 2026-04-21
- **CVE:** N/A
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PublicCMS
- **Affected Products:** PublicCMS
- **Credit:** Vinicius Ribeiro Ferreira da Silva
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-295/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PublicCMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getXml method. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

4/26/24 - ZDI reported the vulnerability to the vendor 8/21/24 – ZDI asked for updates 11/10/25 - ZDI asked for updates 04/17/26 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-04-26 - Vulnerability reported to vendor
- 2026-04-21 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
