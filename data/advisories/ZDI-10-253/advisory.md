# ZDI-10-253: Apple QuickTime GIF LZW Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-253
- **ZDI-CAN:** ZDI-CAN-828
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3795
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required in that a target must open a malicious media file or visit a malicious page. The specific flaw exists within the application's implementation of the LZW compression when opening a certain file format. The application will allocate a buffer for the image and then decompress image data into it. Due to explicitly trusting the decompressed data, a buffer overflow will occur. This can lead to memory corruption and code execution under the context of the application.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
