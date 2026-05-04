# ZDI-11-311: Apple Quicktime Empty URL Data Handler Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-311
- **ZDI-CAN:** ZDI-CAN-1219
- **Date:** 2011-10-27
- **CVE:** CVE-2011-3220
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-311/
## Vulnerability Details

This vulnerability allows remote attackers to potentially disclose memory addresses on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how QuickTime.qts parses a data handler in specific atom within a .mov file. The application will utilize a string length to copy data into an heap buffer, if the string is of zero-length, the application will fail to copy anything and then proceed to use the uninitialized buffer as a string.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5002

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-27 - Coordinated public release of advisory
