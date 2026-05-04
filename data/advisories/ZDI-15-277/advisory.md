# ZDI-15-277: Apple QuickTime SGI Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-277
- **ZDI-CAN:** ZDI-CAN-2589
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3661
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-277/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SGI files. The issue lies in the failure to ensure that image data does not exceed the bounds specified by the header. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user currently logged in.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2014-10-31 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
