# ZDI-14-042: Hewlett-Packard Application Information Optimizer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-042
- **ZDI-CAN:** ZDI-CAN-1656
- **Date:** 2014-04-03
- **CVE:** CVE-2013-6203
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Information Optimizer
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Application Information Optimizer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ability to access configuration pages without authentication. The issue lies in a failure to remove files after the initial configuration has occurred. An attacker can leverage this vulnerability to execute code under the context of the user running the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04140965

## Disclosure Timeline

- 2013-10-14 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
