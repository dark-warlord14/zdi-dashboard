# ZDI-11-197: Microsoft Internet Explorer vgx.dll imagedata Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-197
- **ZDI-CAN:** ZDI-CAN-1070
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1266
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within vgx.dll while parsing VML objects from the DOM. Specifically, the faulty code exists while handling imagedata parameters during page deconstruction. By dynamically assigning an attribute to an imagedata object the process can be made to access freed memory. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-052.mspx

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
