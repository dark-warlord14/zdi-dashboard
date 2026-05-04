# ZDI-20-765: (0Day) CentOS Web Panel ajax_list_accounts username SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-765
- **ZDI-CAN:** ZDI-CAN-9717
- **Date:** 2020-06-25
- **CVE:** CVE-2020-15618
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** CentOS Web Panel
- **Affected Products:** CentOS Web Panel
- **Credit:** @PaulosYibelo & CasperTea
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-765/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of CentOS Web Panel. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_list_accounts.php. When parsing the username parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/31/20 – ZDI reported the vulnerabilities to the vendor 04/30/20 – ZDI requested a status update 05/04/20 – The vendor requested technical clarification 05/05/20 – ZDI provided the requested details 05/08/20 – The vendor indicated they had a fix for the issues 05/20/20 – ZDI asked the vendor for confirmation of a public release date 05/28/20 – ZDI requested a status update 06/12/20 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 06/25/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-01-31 - Vulnerability reported to vendor
- 2020-06-25 - Coordinated public release of advisory
