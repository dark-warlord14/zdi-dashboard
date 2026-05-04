# ZDI-18-1064: (0Day) Quest KACE Systems Management run_cross_report ID SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1064
- **ZDI-CAN:** ZDI-CAN-6097
- **Date:** 2018-09-28
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Quest
- **Affected Products:** KACE Systems Management
- **Credit:** Michael Flanders of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1064/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Quest KACE Systems Management. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the ID parameter provided to the run_cross_report page. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the database.

## Additional Details

Quest has issued an update to correct this vulnerability. More details can be found at: https://support.quest.com/kb/261499/zero-day-initiative-zdi-report-update resolved as of version 9.0.270 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/13/18 - ZDI reported the vulnerabilities to the vendor 09/12/18 - ZDI notified the vendor of the intention to disclose the report as 0-day on 9/18/18 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-09-21 - Vulnerability reported to vendor
- 2018-09-28 - Coordinated public release of advisory
- 2018-10-01 - Advisory Updated
