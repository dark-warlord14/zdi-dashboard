# ZDI-24-841: (0Day) Zope CMFCore Uncontrolled Resource Consumption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-841
- **ZDI-CAN:** ZDI-CAN-21491
- **Date:** 2024-06-21
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Zope
- **Affected Products:** Zope
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-841/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Zope Application Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the contentFilter class. The issue results from uncontrolled resource consumption. An attacker can leverage this vulnerability to create a denial-of-service condition on the server.

## Additional Details

07/13/23 – ZDI reported the vulnerability to the vendor 11/15/23 – ZDI asked for updates 12/19/23 – ZDI asked for updates 06/20/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-07-13 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
