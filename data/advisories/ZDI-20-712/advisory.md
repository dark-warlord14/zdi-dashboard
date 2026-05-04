# ZDI-20-712: (0Day) NETGEAR R6700 httpd Firmware Upload Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-712
- **ZDI-CAN:** ZDI-CAN-9703
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** d4rkn3ss from VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-712/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/08/20 - ZDI reported the vulnerability to the vendor 04/30/20 - ZDI contacted the vendor requesting a status update 05/01/20 - The vendor requested an extension until the end of June 05/05/20 - ZDI agreed on extension until June 15th 05/28/20 - ZDI requested a status update 05/29/20 - The vendor requested an extension until the end of June 05/29/20 - ZDI declined the request and notified the vendor the case would be published as 0-day on 06/15/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-01-08 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
