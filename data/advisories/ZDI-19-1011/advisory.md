# ZDI-19-1011: (0Day) NETGEAR AC1200 mini_httpd Password Storage Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1011
- **ZDI-CAN:** ZDI-CAN-8615
- **Date:** 2019-12-12
- **CVE:** N/A
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** AC1200
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1011/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on vulnerable installations of NETGEAR AC1200 Smart WiFi Router. Authentication is required to exploit this vulnerability. The specific flaw exists within the storage of administrator credentials. The credentials are stored in a recoverable format making them subject to password reuse attacks. An attacker can leverage this vulnerability to disclose sensitive information in the context of the administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/27/19 – ZDI reported the vulnerability to the vendor 06/27/19 – The vendor acknowledged the report 07/04/19 – The vendor confirmed the report as valid 08/28/19 – ZDI requested an update 08/29/19 – The vendor indicated they were working on a fix 10/08/19 – ZDI requested an update 10/10/19 – ZDI asked if a fix for a similar case included the fix for this one 10/11/19 – The vendor indicated the fix was not included 10/17/19 – ZDI requested an ETA for resolution 11/11/19 – ZDI requested an update 11/29/19 – ZDI requested an update 12/05/19 – ZDI advised the vendor of the intention to publish the report as a 0-day on 12/12/2019 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-04-26 - Vulnerability reported to vendor
- 2019-12-12 - Coordinated public release of advisory
