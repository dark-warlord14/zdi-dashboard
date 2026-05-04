# ZDI-11-005: HP OpenView Network Node Manager ovas.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-005
- **ZDI-CAN:** ZDI-CAN-774
- **Date:** 2011-01-10
- **CVE:** CVE-2011-0263
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** SilentSignal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-005/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The flaw exists within the ovas.exe component which listens by default on TCP port 7510. When handling the Source Node or Destination Node name POST variables the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the OVAS service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02670501

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-01-10 - Coordinated public release of advisory
