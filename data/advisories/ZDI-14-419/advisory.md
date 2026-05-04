# ZDI-14-419: BMC Track-It! Web Account Credential Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-419
- **ZDI-CAN:** ZDI-CAN-2581
- **Date:** 2014-12-09
- **CVE:** CVE-2014-8270
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** BMC Software
- **Affected Products:** Track-It!
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-419/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BMC Track-It!. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of password resets. The issue lies in the ability to register an account matching the name of a local account on the system and then reset the password for it. An attacker can leverage this vulnerability to gain credentials for the Administrator account on the system.

## Additional Details

BMC Software has issued an update to correct this vulnerability. More details can be found at: http://support.numarasoftware.com/support/view_article.asp?ArticleID=7654

## Disclosure Timeline

- 2014-11-05 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
