# ZDI-10-083: HP OpenView NNM snmpviewer.exe CGI Multiple Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-083
- **ZDI-CAN:** ZDI-CAN-566
- **Date:** 2010-05-11
- **CVE:** CVE-2010-1552
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the snmpviewer.exe CGI. The doLoad function in this process calls sprintf() with a %s format specifier and unsanitized user input retrieved from two separate POST variables (act and app). By providing large enough strings a remote attacker can cause a stack-based buffer overflow and eventually execute arbitrary code under the context of the webserver process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02153379

## Disclosure Timeline

- 2010-02-11 - Vulnerability reported to vendor
- 2010-05-11 - Coordinated public release of advisory
