# ZDI-11-231: Apple QuickTime Pict File Matrix Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-231
- **ZDI-CAN:** ZDI-CAN-1148
- **Date:** 2011-06-29
- **CVE:** CVE-2010-3790
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Subreption LLC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a Matrix structure within a particular opcode embedded within a .pict file. When using this Matrix structure to transform image data, the application will miscalculate an index to represent a row of an object. This will cause the application to write outside the bounds of the array of objects which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4723

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-06-29 - Coordinated public release of advisory
