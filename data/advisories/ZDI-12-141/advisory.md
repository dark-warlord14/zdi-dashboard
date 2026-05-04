# ZDI-12-141: Microsoft .NET Framework Clipboard Unsafe Memory Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-141
- **ZDI-CAN:** ZDI-CAN-1469
- **Date:** 2012-08-17
- **CVE:** CVE-2012-1855
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-141/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the .NET Framework. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within Microsoft .NET XAML Browser Application (XBAP) handling of Clipboard object data. It is possible to cause unsafe memory access within System.Windows.Forms.Clipboard, allowing an attacker to control the memory used by an object's native code. This unsafe access allows for control of a function pointer, which can be exploited to remotely execute code. In the case of Internet Explorer, execution of attacker code occurs outside of the Protected Mode sandbox.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-038

## Disclosure Timeline

- 2012-01-12 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
