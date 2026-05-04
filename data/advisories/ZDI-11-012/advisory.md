# ZDI-11-012: Hewlett-Packard OpenView Network Node Manager nnmRptConfig.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-012
- **ZDI-CAN:** ZDI-CAN-936
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0270
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Aniway
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within nnmRptConfig.exe CGI which is exposed by the webserver which listens by default on TCP port 80. When parsing an invalid template name the application uses user supplied data as a format specifier during creation of an error message. An attacker can exploit this vulnerability by supplying a specially crafted and invalid template name to execute arbitrary code under the context of the user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
