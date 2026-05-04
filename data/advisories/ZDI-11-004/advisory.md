# ZDI-11-004: HP OpenView Network Node Manager ovutil.dll stringToSeconds Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-004
- **ZDI-CAN:** ZDI-CAN-757
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0262
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The exploit would require a crafted HTTP request to the target host. The specific flaw exists within the ovutil.dll module which is loaded by the ovwebsnmpsrv.exe process which in turn can be reached remotely through the jovgraph.exe CGI program. By supplying overly large values to variables passed through an HTTP request a sscanf can be made to overflow a static buffer. An attacker can leverage this to execute arbitrary code under the context of the user running the webserver.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
