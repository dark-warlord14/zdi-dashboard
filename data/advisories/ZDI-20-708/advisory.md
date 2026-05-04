# ZDI-20-708: (0Day) NETGEAR R6700 httpd strtblupgrade Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-708
- **ZDI-CAN:** ZDI-CAN-9767
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** d4rkn3ss from VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-708/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of string table file uploads. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/05/20 – ZDI disclosed the vulnerability reports to the vendor 03/27/20 – The vendor requested an extension until the end of May 05/29/20 – The vendor requested an extension until the end of June 05/29/20 – ZDI declined the request and notified the vendor the cases would be published as 0-day advisories on 06/08/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-02-05 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
