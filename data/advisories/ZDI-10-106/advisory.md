# ZDI-10-106: Hewlett-Packard OpenView NNM ovutil.dll getProxiedStorageAddress Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-106
- **ZDI-CAN:** ZDI-CAN-685
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1961
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ovutil.dll module which is loaded by the ovwebsnmpsrv.exe process which in turn can be reached remotely through the jovgraph.exe CGI program. By supplying overly large values to variables passed through an HTTP request a sprintf can be made to overflow a static buffer. An attacker can leverage this to execute arbitrary code under the context of the user running the webserver.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02217439

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
