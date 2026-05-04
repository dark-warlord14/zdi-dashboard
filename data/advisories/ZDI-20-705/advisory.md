# ZDI-20-705: (0Day) (Pwn2Own) NETGEAR R6700 check_ra Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-705
- **ZDI-CAN:** ZDI-CAN-9647
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-705/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloading of files via HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/14/19 – ZDI reported the vulnerabilities to the vendor 11/20/19 – The vendor asked for clarification on the submissions 11/20/19 – ZDI provided the details 03/25/20 – ZDI requested a status update 03/27/20 – The vendor requested an extension until the end of May 03/30/20 – ZDI agreed on the extension 05/28/20 – ZDI requested a status update 05/29/20 – The vendor requested an extension until the end of June 05/29/20 – ZDI declined the request and notified the vendor the cases would be published as 0-day advisories on 06/08/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-11-15 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
