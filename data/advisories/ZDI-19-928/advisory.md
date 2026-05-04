# ZDI-19-928: (0Day) Jenkins ElasticBox CI Cleartext Storage of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-928
- **ZDI-CAN:** ZDI-CAN-8880
- **Date:** 2019-10-30
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Jenkins
- **Affected Products:** ElasticBox CI
- **Credit:** David Fiser (Trend Micro Team Nebula)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-928/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Jenkins ElasticBox CI. Authentication is required to exploit this vulnerability. The specific flaw exists within the ElasticBox CI plugin. The issue results from storing credentials in plaintext. An attacker can leverage this vulnerability to execute code in the context of the build process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/18/19 - ZDI reported the vulnerability to the vendor 06/18/19 - The vendor acknowledged reception 09/13/19 - ZDI contacted the vendor requesting a status update 09/13/19 - The vendor replied it was in progress 10/03/19 - The vendor communicated all advisories would be published on the due date even if they remained unfixed 10/25/19 - ZDI notified vendor the intention to 0-day the report on 10/30 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2019-06-18 - Vulnerability reported to vendor
- 2019-10-30 - Coordinated public release of advisory
