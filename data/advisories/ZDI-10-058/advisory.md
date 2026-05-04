# ZDI-10-058: Apple Mac OS X ImageIO Framework JPEG2000 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-058
- **ZDI-CAN:** ZDI-CAN-634
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0505
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** 85319bb6e6ab398b334509c50afce5259d42756e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Mac OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Apple ImageIO framework during the parsing of malformed JPEG2000 files. The function CGImageReadGetBytesAtOffset can utilize miscalculated values during a memmove operation that will result in an exploitable heap corruption allowing attackers to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
