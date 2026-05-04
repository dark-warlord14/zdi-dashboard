# ZDI-13-200: Hewlett-Packard Application Lifecycle Management Quality Center Multiple Cross-Site Scripting Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-13-200
- **ZDI-CAN:** ZDI-CAN-1565
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4802
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Lifecycle Management
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary client side script on vulnerable installations of HP Application Lifecycle Management Quality Center. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of html messages sent to HP Application Lifecycle Management Quality Center. Messages are improperly sanitized allowing an attacker to inject arbitrary javascript into the page. This can be abused by an attacker to perform a cross-site scripting attack on the user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03864640

## Disclosure Timeline

- 2013-02-01 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
