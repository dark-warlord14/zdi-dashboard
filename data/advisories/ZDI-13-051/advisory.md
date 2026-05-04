# ZDI-13-051: Hewlett-Packard Intelligent Management Center FaultDownloadServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-051
- **ZDI-CAN:** ZDI-CAN-1612
- **Date:** 2013-03-22
- **CVE:** CVE-2012-5202
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-051/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FaultDownloadServlet. Authentication is not required to access this servlet, which allows any file readable by SYSTEM to be disclosed. By abusing this behavior an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03689276

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
