# ZDI-11-173: Novell iPrint nipplib.dll profile-time Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-173
- **ZDI-CAN:** ZDI-CAN-1127
- **Date:** 2011-06-06
- **CVE:** CVE-2011-1700
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-173/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib component which is used by both the ActiveX and Netscape compatible browser plugins. When handling the profile-time parameter from the user specified printer-url the process blindly copies user supplied data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix has been documented as 7008722: Security Vulnerability - Novell iPrint nipplib.dll profile-time Remote Code Execution Vulnerability http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7008722

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-06-06 - Coordinated public release of advisory
