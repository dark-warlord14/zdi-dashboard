# ZDI-11-313: Apple QuickTime FLC RLE Packet Count Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-313
- **ZDI-CAN:** ZDI-CAN-1274
- **Date:** 2011-10-27
- **CVE:** CVE-2011-3223
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk Anonymous pa_kt / twitter.com/pa_kt / e1c14ba6
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-313/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime decodes flic file. Flic files can contain FLC Delta Decompression block containing Run Length Encoded data. When Quicktime tries to decompress this data it reads a user supplied RLE Packet count field from the file and uses that as loop counter. A high value for this field will cause Quicktime to write outside previously allocated memory which could result into remote code execution.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5002

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-10-27 - Coordinated public release of advisory
