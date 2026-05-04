# ZDI-10-043: Apple QuickTime FlashPix NumberOfTiles Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-043
- **ZDI-CAN:** ZDI-CAN-597
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0519
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of a malformed SubImage Header Stream from a malicious FlashPix image. The application takes the NumberOfTiles field from this data structure, multiplies it by 16, and then uses it in an allocation. If this result is larger than 32-bits the value will wrap leading to an under-allocated buffer. Later when the application copies data into this buffer, a buffer overflow will occur leading to code execution within the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
