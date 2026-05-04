# ZDI-09-029: Apple QuickTime Jpeg2000 Marker Size Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-029
- **ZDI-CAN:** ZDI-CAN-480
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0957
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of malformed Jpen2000 image files. A field is read directly from the file and used to allocate memory for a structure. If the value read is smaller then the expected structure size then a memory corruption will occur which can be leveraged by an attacker to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
