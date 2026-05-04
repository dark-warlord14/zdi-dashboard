# ZDI-10-137: Hewlett-Packard OpenView NNM webappmon.exe execvp_nc Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-137
- **ZDI-CAN:** ZDI-CAN-682
- **Date:** 2010-07-21
- **CVE:** CVE-2010-2703
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-137/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ov.dll module which is loaded by the webappmon.exe CGI program. This DLL defines a function execvp_nc which unsafely concatenates a controllable command string into a statically allocated stack buffer. By supplying overly large values to variables passed through an HTTP request a strcat_new can be made to overflow this buffer. An attacker can leverage this to execute arbitrary code under the context of the user running the webserver.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02286088

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-07-21 - Coordinated public release of advisory
