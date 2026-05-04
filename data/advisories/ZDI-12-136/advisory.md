# ZDI-12-136: Apple QuickTime Invalid Public Movie Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-136
- **ZDI-CAN:** ZDI-CAN-1371
- **Date:** 2012-08-17
- **CVE:** CVE-2011-3220
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's QuickTime player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within how the application handles a malformed atom type when playing a movie encoded with uncompressed audio. When decoding the audio sample the application will use a 16-bit length for allocating a buffer, and a different one for initializing it. This can cause memory corruption which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
