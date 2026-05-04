# ZDI-13-055: Apple Mac OS X PDF Ink Annotations Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-055
- **ZDI-CAN:** ZDI-CAN-1518
- **Date:** 2013-04-09
- **CVE:** CVE-2013-0971
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Tobias Klein
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a PDF file. During the processing of a specific InkList array, a reference is created to an object that is freed before use. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-14 - Vulnerability reported to vendor
- 2013-04-09 - Coordinated public release of advisory
