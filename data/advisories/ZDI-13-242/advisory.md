# ZDI-13-242: Hewlett-Packard Intelligent Management Center SOM sdFileDownload Servlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-242
- **ZDI-CAN:** ZDI-CAN-1647
- **Date:** 2013-10-16
- **CVE:** CVE-2013-4826
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-242/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sdFileDownload servlet. Authentication is not required to access this servlet, which allows any file readable by SYSTEM to be disclosed. By abusing this behavior an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03943547

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
