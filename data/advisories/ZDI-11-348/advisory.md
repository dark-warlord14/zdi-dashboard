# ZDI-11-348: HP OpenView NNM nnmRptConfig.exe nameParams Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-348
- **ZDI-CAN:** ZDI-CAN-1208
- **Date:** 2011-12-13
- **CVE:** CVE-2011-3165
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-348/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within nnmRotConfig.exe CGI program. When processing crafted nameParams parameters, there exists an insufficient boundary check that can lead to a insufficient heap buffer, enabling a heap overflow. This can lead to memory corruption which can be leveraged to execute arbitrary code under the context of the target service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03054052

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-12-13 - Coordinated public release of advisory
