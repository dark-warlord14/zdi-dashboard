# ZDI-09-084: Apple Quicktime FIRE Codec Heap Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-084
- **ZDI-CAN:** ZDI-CAN-481
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0954
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application decodes a .MOV file containing a frame encoded with Quicktime's FIRE codec. While decoding the frame's contents, the application will trust the frame data contains a special terminator during copying of file data to a heap buffer. If the terminator is not found, the application will copy indefinitely. This can result in a heap overflow which can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2009-04-20 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
