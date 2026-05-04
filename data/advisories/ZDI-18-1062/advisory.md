# ZDI-18-1062: Quest KACE Systems Management run_report SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1062
- **ZDI-CAN:** ZDI-CAN-6075
- **Date:** 2018-09-18
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Quest
- **Affected Products:** KACE Systems Management
- **Credit:** Alain Homewood (Insomnia Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1062/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Quest KACE Systems Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the ID parameter provided to the run_report page. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the database.

## Additional Details

Quest has issued an update to correct this vulnerability. More details can be found at: https://support.quest.com/kace-systems-management-appliance/kb/254193/security-vulnerability-patch-sec2018_20180410-

## Disclosure Timeline

- 2018-04-11 - Vulnerability reported to vendor
- 2018-09-18 - Coordinated public release of advisory
- 2018-09-28 - Advisory Updated
