# ZDI-11-248: Microsoft Internet Explorer 9 STYLE Object Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-248
- **ZDI-CAN:** ZDI-CAN-1244
- **Date:** 2011-08-09
- **CVE:** CVE-2011-1964
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the part of the application that is responsible for handling STYLE elements. By creating a STYLE element with an invalid behavior, an attacker can force an object of invalid type to be called, resulting in corruption of heap memory. This can be leveraged by an attacker to achieve code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-057.mspx

## Disclosure Timeline

- 2011-05-25 - Vulnerability reported to vendor
- 2011-08-09 - Coordinated public release of advisory
