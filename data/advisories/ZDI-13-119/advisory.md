# ZDI-13-119: Apple QuickTime FlashPix Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-119
- **ZDI-CAN:** ZDI-CAN-1710
- **Date:** 2013-06-11
- **CVE:** CVE-2013-0988
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of FlashPix files. While parsing FlashPix files, a length is multiplied by four when allocating the buffer but is multiplied by eight when copying data into the buffer. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
