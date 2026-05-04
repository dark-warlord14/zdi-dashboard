# ZDI-13-113: Apple QuickTime 3GP Parsing Remote Code Execution Vunerability

## Metadata

- **ZDI ID:** ZDI-13-113
- **ZDI-CAN:** ZDI-CAN-1641
- **Date:** 2013-06-11
- **CVE:** CVE-2013-1018
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of H.264 compressed data. Lengths specified within the file are not properly validated before being used as a size in a memory copy. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
