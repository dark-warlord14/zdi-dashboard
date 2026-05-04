# ZDI-12-131: Microsoft .NET Framework Undersized Glyph Buffer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-131
- **ZDI-CAN:** ZDI-CAN-1432
- **Date:** 2012-08-03
- **CVE:** CVE-2012-0162
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-131/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the .NET Framework. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Microsoft .NET handling of XAML Browser Applications (XBAP) graphics components. It is possible to cause an undersized allocation for a buffer which is populated with user-supplied glyph data, resulting in memory corruption which can be leveraged to remotely execute code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-034

## Disclosure Timeline

- 2011-12-07 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
