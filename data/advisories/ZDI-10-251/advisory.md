# ZDI-10-251: Apple QuickTime FlashPix Max Uninitialized Jpeg Table Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-251
- **ZDI-CAN:** ZDI-CAN-778
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3794
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support for huffman tables within a flashpix file. By specifying an index larger than a particular value, a pointer will cease to get initialized. Later the application will use this pointer to as the destination in a copy operation. Successful exploitation will lead to code execution under the context of the application.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
