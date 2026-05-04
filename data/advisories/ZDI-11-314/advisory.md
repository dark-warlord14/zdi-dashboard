# ZDI-11-314: Apple Quicktime PnPixPat PatType 3 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-314
- **ZDI-CAN:** ZDI-CAN-1090
- **Date:** 2011-10-27
- **CVE:** CVE-2011-3247
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-314/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a specific opcode within a PCT file. When resizing a heap buffer, the application will use a signed word read from the file to calculate the resulting size. This can be used to force the target buffer to be of an undersized length. Usage of this buffer will result in a buffer overflow in the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5016

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-10-27 - Coordinated public release of advisory
