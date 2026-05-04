# ZDI-12-003: HP OpenView NNM webappmon.exe parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-003
- **ZDI-CAN:** ZDI-CAN-1209
- **Date:** 2012-01-05
- **CVE:** CVE-2011-3166
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within webappmon.exe CGI program. When processing crafted parameters, there exists an insufficient boundary check before supplying a format string with the values, causing a stack overflow. This can lead to memory corruption which can be leveraged to execute arbitrary code under the context of the target service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03054052

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2012-01-05 - Coordinated public release of advisory
