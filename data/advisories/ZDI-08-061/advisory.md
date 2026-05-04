# ZDI-08-061: Apple QuickTime Player H.264 Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-061
- **ZDI-CAN:** ZDI-CAN-309
- **Date:** 2008-09-09
- **CVE:** CVE-2008-3627
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of MP4 video files in QuickTimeH264.qtx. A maliciously crafted MDAT atom can cause a heap corruption resulting in the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3027

## Disclosure Timeline

- 2008-05-13 - Vulnerability reported to vendor
- 2008-09-09 - Coordinated public release of advisory
