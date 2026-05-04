# ZDI-10-199: Microsoft Windows Media Player Network Sharing Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-199
- **ZDI-CAN:** ZDI-CAN-854
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3225
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player 11
- **Credit:** Oleksandr Mirosh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-199/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. Authentication is not required to exploit this vulnerability. The specific flaw exists within Windows Media Player's support for streaming media to other equipment located on the same network. If a specially formatted RTSP request is made to an instance of the application's streaming service, the application will free an object, and then later reuse it. This can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-075.mspx

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
