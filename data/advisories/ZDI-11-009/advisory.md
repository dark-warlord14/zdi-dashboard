# ZDI-11-009: Hewlett-Packard OpenView Network Node Manager nnmRptConfig.exe schdParams/nameParams Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-009
- **ZDI-CAN:** ZDI-CAN-933
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0267
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Aniway (Aniway.Anyway AT gmail DOT com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nnmRptConfig.exe module exposed by the webserver that listens by default on TCP port 80. A remote user can send an oversized schdParams or nameParams parameter via a POST request to one of the CGI functions of NNM to trigger a buffer overflow in this module. Exploitation of this issue leads to remote code execution under the context of the target service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
