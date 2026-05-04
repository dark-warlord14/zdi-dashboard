# ZDI-11-180: Novell iPrint op-printer-list-all-jobs cookie Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-180
- **ZDI-CAN:** ZDI-CAN-1134
- **Date:** 2011-06-06
- **CVE:** CVE-2011-1708
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-180/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib component which is used by both the ActiveX and Netscape compatible browser plugins. When handling the op-printer-list-all-jobs parameter from the user specified printer-url the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix has been documented as TID 7008731: Security Vulnerability - Novell iPrint op-printer-list-all-jobs cookie Remote Code Execution Vulnerability http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7008731

## Disclosure Timeline

- 2011-04-06 - Vulnerability reported to vendor
- 2011-06-06 - Coordinated public release of advisory
