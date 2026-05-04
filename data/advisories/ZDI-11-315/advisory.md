# ZDI-11-315: Apple QuickTime FLC Delta Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-315
- **ZDI-CAN:** ZDI-CAN-1275
- **Date:** 2011-10-27
- **CVE:** CVE-2011-3249
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-315/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime decodes flic file. Flic files can contain FLC Delta Decompression block containing Run Length Encoded data. Quicktime fails to correctly checking the decompression size when decoding the RLE data. This allowes for a 4 byte overwrite past the end of the buffer which could result into remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5016

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-10-27 - Coordinated public release of advisory
