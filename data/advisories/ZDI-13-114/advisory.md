# ZDI-13-114: Apple QuickTime MJPEG Frame stsd Atom Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-114
- **ZDI-CAN:** ZDI-CAN-1720
- **Date:** 2013-06-11
- **CVE:** CVE-2013-1020
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher (Microsoft) & Paul Bates (Microsoft)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-114/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing a mjpeg movie with an improper jpeg frame size via the stsd atom. When processing the movie, the size of the destination buffer for jpeg contents is specified separately from the JPEG size. This can lead to memory corruption that can be leveraged to achieve code execution under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-02-04 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
