# ZDI-09-021: Apple QuickTime PICT Unspecified Tag Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-021
- **ZDI-CAN:** ZDI-CAN-470
- **Date:** 2009-05-13
- **CVE:** CVE-2009-0010
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put, Sebastian Apelt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application parses a malformed .PICT image. While decoding a tag 0x77 in the image, the application misuses a 16-bit length when allocating tag data. When copying tag data into this buffer, a heap overflow occurs. This can lead to code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3549

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2009-05-13 - Coordinated public release of advisory
