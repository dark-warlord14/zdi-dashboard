# ZDI-14-041: Hewlett-Packard Application Information Optimizer Credential Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-041
- **ZDI-CAN:** ZDI-CAN-2004
- **Date:** 2014-04-03
- **CVE:** CVE-2013-6204
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Information Optimizer
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Application Information Optimizer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the password reset functionality. It is possible for an attacker to reach this function in such a way that the password of a random account on the system will be reset, and both the account name and new password will be returned to the attacker.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04140965

## Disclosure Timeline

- 2013-12-22 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
