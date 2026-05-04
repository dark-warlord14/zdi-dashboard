# ZDI-10-105: Hewlett-Packard OpenView NNM ovwebsnmpsrv.exe Bad Option Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-105
- **ZDI-CAN:** ZDI-CAN-684
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1960
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ovwebsnmpsrv.exe process which can be reached remotely through the jovgraph.exe CGI program. When the ovwebsnmpsrv.exe process is started a function responsible for parsing command line arguments does not properly handle unrecognized options. By supplying an overly large unrecognized option through an HTTP request the error handling functionality can be made to overflow a static buffer while creating the error message. An attacker can leverage this to execute arbitrary code under the context of the user running the webserver.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02217439

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
