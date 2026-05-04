# ZDI-20-704: (0Day) (Pwn2Own) NETGEAR R6700 UPnP NewBlockSiteName Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-704
- **ZDI-CAN:** ZDI-CAN-9643
- **Date:** 2020-06-15
- **CVE:** CVE-2020-10924
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-704/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R6700 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the UPnP service, which listens on TCP port 5000 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/14/19 – ZDI reported the vulnerabilities to the vendor 11/20/19 – The vendor asked for clarification on the submissions 11/20/19 – ZDI provided the details 03/25/20 – ZDI requested a status update 03/27/20 – The vendor requested an extension until the end of May 03/30/20 – ZDI agreed on the extension 05/28/20 – ZDI requested a status update 05/29/20 – The vendor requested an extension until the end of June 05/29/20 – ZDI declined the request and notified the vendor the cases would be published as 0-day advisories on 06/08/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-11-14 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
