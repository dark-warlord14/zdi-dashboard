# ZDI-13-117: Apple QuickTime H.263 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-117
- **ZDI-CAN:** ZDI-CAN-1604
- **Date:** 2013-06-11
- **CVE:** CVE-2013-1016
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher Microsoft & Paul Bates Microsoft
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of H.263 data. The H.263 data is not properly validated which can result in writing past an intended buffer. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
