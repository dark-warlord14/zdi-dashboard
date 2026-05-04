# ZDI-09-063: Apple QuickTime H.264 Nal Unit Length Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-063
- **ZDI-CAN:** ZDI-CAN-500
- **Date:** 2009-09-10
- **CVE:** CVE-2009-2799
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of samples from a malformed MOV file utilizing the H.264 codec. While parsing data to render the stream, the application will mistrust a length that is used to initialize a heap chunk that was allocated in a header. If the length is larger than the size of the chunk allocated, then a memory corruption will occur leading to code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3859

## Disclosure Timeline

- 2009-07-28 - Vulnerability reported to vendor
- 2009-09-10 - Coordinated public release of advisory
