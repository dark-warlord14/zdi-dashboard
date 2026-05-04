# ZDI-12-103: Apple Quicktime Dataref URI Buffer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-103
- **ZDI-CAN:** ZDI-CAN-1369
- **Date:** 2012-06-27
- **CVE:** CVE-2011-3459
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-103/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw occurs when parsing a movie file containing multiple atoms with a different string length. When resizing a buffer in order to make space for the string, the application will forget to include the null-terminator. When the application attempts to null-terminate the string, an out-of-bounds write will occur. If an aggressor can place the a useful heap buffer contiguous to the reallocated string, this can lead to code execution under the context of the applicaiton.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5130

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-27 - Coordinated public release of advisory
