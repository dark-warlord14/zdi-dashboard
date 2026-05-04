# ZDI-13-168: Microsoft Windows Media Player WMV Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-168
- **ZDI-CAN:** ZDI-CAN-1592
- **Date:** 2013-07-26
- **CVE:** CVE-2013-3127
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** FuzzMyApp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-168/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the ASF Header Object where the initial value of a for loop is not properly sanitized. An integer underflow can occur resulting in a buffer overflow. This can be leveraged to gain remote code execution under the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-057

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
