# ZDI-13-112: Apple QuickTime TeXML textBox Element Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-112
- **ZDI-CAN:** ZDI-CAN-1628
- **Date:** 2013-06-11
- **CVE:** CVE-2013-1015
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Apple QuickTime handles textBox elements within a TeXML file. Specifically, the code within QuickTime.qts does not properly validate the coordinate values of the x and y attributes. By providing specially crafted coordinate values, the code can be made to write data ahead of a buffer, leading to memory corruption. This memory corruption could lead to remote code execution under that context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
