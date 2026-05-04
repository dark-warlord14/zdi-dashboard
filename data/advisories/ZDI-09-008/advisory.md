# ZDI-09-008: Apple QuickTime STSD JPEG Atom Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-008
- **ZDI-CAN:** ZDI-CAN-352
- **Date:** 2009-01-21
- **CVE:** CVE-2009-0007
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the handling of JPEG atoms embedded in STSD atoms within the function JPEG_DComponentDispatch(). When the image width data in this atom is modified, a heap corruption occurs which can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3403

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2009-01-21 - Coordinated public release of advisory
