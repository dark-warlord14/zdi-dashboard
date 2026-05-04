# ZDI-13-060: Hewlett-Packard Intelligent Management Center flexFileUpload Servlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-060
- **ZDI-CAN:** ZDI-CAN-1659
- **Date:** 2013-04-09
- **CVE:** CVE-2012-5209
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the flexFileUpload servlet. This servlet exposes file upload functionalities and suffers from a directory traversal vulnerability which allows a file to be written to the server. By abusing this behavior an attacker can place a file and leverage the situation to achieve remote code execution as the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03689276

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-04-09 - Coordinated public release of advisory
