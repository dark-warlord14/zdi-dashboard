# ZDI-15-239: Hewlett-Packard SiteScope Log Analyzer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-239
- **ZDI-CAN:** ZDI-CAN-2567
- **Date:** 2015-05-26
- **CVE:** CVE-2015-2120
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-239/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on vulnerable installations of Hewlett-Packard SiteScope. Authentication is required to exploit this vulnerability. The specific flaw exists within the Log Analysis Tool. This tool does not validate or restrict the log path allowing users to read the users.config file. A remote attacker can leverage this vulnerability to escalate privileges from the user to administrator role.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04688784

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-05-26 - Coordinated public release of advisory
