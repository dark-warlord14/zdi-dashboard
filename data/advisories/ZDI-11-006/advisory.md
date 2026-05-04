# ZDI-11-006: Hewlett-Packard Network Node Manager OVutil.dll Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-006
- **ZDI-CAN:** ZDI-CAN-810
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0264
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** SilentSignal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The flaw exists within the ovutil.dll component which is loaded by the webserver listening by default on TCP port 80. When handling the COOKIE variable passed through a GET request, the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
