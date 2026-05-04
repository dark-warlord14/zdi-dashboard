# ZDI-19-1014: (0Day) NETGEAR AC1200 mini_httpd Cleartext Transmission of Sensitive Information Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1014
- **ZDI-CAN:** ZDI-CAN-8671
- **Date:** 2019-12-12
- **CVE:** N/A
- **CVSS:** 5.7
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** AC1200
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1014/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of NETGEAR AC1200 Smart WiFi Router. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of admin credentials provided to the mini_httpd endpoint. The issue results from displaying sensitive information in plaintext. An attacker can leverage this vulnerability to disclose sensitive information in the context of the administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/27/19 – ZDI reported the vulnerability to the vendor 06/27/19 – The vendor acknowledged 10/08/19 – ZDI requested a new update 10/10/19 – ZDI asked if a fix for a similar case included the fix for this one 10/11/19 – The vendor indicated the fix was not included 10/17/19 – ZDI requested an ETA for resolution and remarked the case was due in 10 days 11/11/19 – ZDI requested a new update and indicated the case was due 11/29/19 – ZDI requested an update 12/05/19 – ZDI communicated the vendor the intention to 0-day the case on December 12th -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-06-27 - Vulnerability reported to vendor
- 2019-12-12 - Coordinated public release of advisory
