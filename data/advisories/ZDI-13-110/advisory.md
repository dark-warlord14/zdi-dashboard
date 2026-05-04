# ZDI-13-110: Apple QuickTime dref Volume Name Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-110
- **ZDI-CAN:** ZDI-CAN-1602
- **Date:** 2013-05-30
- **CVE:** CVE-2013-1017
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher (Microsoft) & Paul Bates (Microsoft)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a MOV file. A dref atom can contain information specifying a past location of the MOV file. A value within this atom is used to determine how many bytes to copy into a buffer without ensuring that the value is smaller than the size of the buffer, resulting in an overflow. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
