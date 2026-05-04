# ZDI-26-033: (0Day) Open WebUI Cleartext Transmission of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-033
- **ZDI-CAN:** ZDI-CAN-28259
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0767
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Open WebUI
- **Affected Products:** Open WebUI
- **Credit:** Peter Girnus (@gothburz), Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-033/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Open WebUI. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of credentials provided to the endpoint. The issue results from transmitting sensitive information in plaintext. An attacker can leverage this vulnerability to disclose transmitted credentials, leading to further compromise.

## Additional Details

10/09/25 – ZDI submitted the report to the vendor’s GitHub account 10/10/25 – the vendor closed the report 10/15/25 – ZDI asked for the reason 11/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-10-09 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
