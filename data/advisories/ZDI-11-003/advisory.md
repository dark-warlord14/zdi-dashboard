# ZDI-11-003: HP OpenView Network Node Manager jovgraph.exe displayWidth Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-003
- **ZDI-CAN:** ZDI-CAN-753
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0261
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The exploit would require a crafted HTTP request to the target host. The specific flaw exists within jovgraph.exe, a Java-based grapher that extends the SNMP Data Presenter to include xnmgraph-like applications created by the application builder. The vulnerability occurs within jovgraph when processing malformed displayWidth option passed from the arg parameter to the CGI program. A remote unauthenticated attacker can send a crafted HTTP request to the target host to exploit this vulnerability. Successful attack could allow for arbitrary code being injected and executed with the privileges of the affected process, normally Internet Guest Account on Windows platforms.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
