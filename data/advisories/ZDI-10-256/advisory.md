# ZDI-10-256: Novell iPrint Activex GetDriverSettings Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-256
- **ZDI-CAN:** ZDI-CAN-959
- **Date:** 2010-12-23
- **CVE:** CVE-2010-4321
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Anonymous gwslabs.com Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the ienipp.ocx component. When handling the exposed method a GetDriverSettings call is made into nipplib!IppGetDriverSettings2 where the process will blindly copy user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix for this security vulnerability is included in the released "iPrint Client for Windows XP/Vista/Win 7 5.56" patch, available at http://download.novell.com/Download?buildid=JV7fd0tFHHM~ .

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2010-12-23 - Coordinated public release of advisory
