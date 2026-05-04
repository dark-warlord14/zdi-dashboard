# ZDI-20-713: (0Day) NETGEAR R6700 httpd strtblupgrade Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-713
- **ZDI-CAN:** ZDI-CAN-9756
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** d4rkn3ss from VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-713/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of string table file uploads. A crafted gui_region in a string table file can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/23/20 - ZDI reported the vulnerability to the vendor 04/30/20 - ZDI contacted the vendor requesting a status update 05/01/20 - The vendor requested an extension until the end of June 05/05/20 - ZDI agreed on extension until June 15th 05/28/20 - ZDI requested a status update 05/29/20 - The vendor requested an extension until the end of June 05/29/20 - ZDI declined the request and notified the vendor the case would be published as 0-day on 06/15/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-01-23 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
