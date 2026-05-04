# ZDI-09-026: Apple QuickTime Packed-bit Decoding Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-026
- **ZDI-CAN:** ZDI-CAN-469
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0952
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application parses a malformed .PSD image. While decoding the columns, rows and channels in the image header, the application trusts a different length for copying than used for allocating it. This results in a heap overflow and can lead to code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
