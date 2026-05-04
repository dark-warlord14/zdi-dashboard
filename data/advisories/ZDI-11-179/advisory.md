# ZDI-11-179: Novell iPrint nipplib.dll iprint-client-config-info Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-179
- **ZDI-CAN:** ZDI-CAN-1133
- **Date:** 2011-06-06
- **CVE:** CVE-2011-1706
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-179/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib component which is used by both the ActiveX and Netscape compatible browser plugins. When handling the iprint-client-config-info parameter from the user specified printer-url the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

TID 7008730: Security Vulnerability - Novell iPrint nipplib.dll iprint-client-config-info Remote Code Execution Vulnerability http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7008730

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-06-06 - Coordinated public release of advisory
