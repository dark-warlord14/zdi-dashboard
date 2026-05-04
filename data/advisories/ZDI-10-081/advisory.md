# ZDI-10-081: HP OpenView NNM ovet_demandpoll sel CGI Variable Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-081
- **ZDI-CAN:** ZDI-CAN-563
- **Date:** 2010-05-11
- **CVE:** CVE-2010-1550
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ovet_demandpoll.exe process. This process can be started by invoking the webappmon.exe CGI application through the webserver. The process calls vnsprintf() directly with the contents of the 'sel' POST variable. By providing a malicious value this format string vulnerability can be leveraged by remote attackers to execute arbitrary code under the context of the ovet_demandpoll.exe process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02153379

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-05-11 - Coordinated public release of advisory
