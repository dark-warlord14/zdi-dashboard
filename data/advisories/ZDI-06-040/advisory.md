# ZDI-06-040: WinZip FileView ActiveX Control Unsafe Method Exposure Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-040
- **ZDI-CAN:** ZDI-CAN-077
- **Date:** 2006-11-14
- **CVE:** CVE-2006-5198
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** WinZip Computing
- **Affected Products:** WinZip
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of WinZip. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the ActiveX control WZFILEVIEW.FileViewCtrl.61, CLSID: A09AE68F-B14D-43ED-B713-BA413F034904 A re-branded version of the "FileView" ActiveX control developed by Sky Software. The object is marked "Safe for Scripting" and exposes several unsafe methods which can be leveraged to result in arbitrary code execution with no further interaction.

## Additional Details

WinZip Computing has issued an update to correct this vulnerability. More details can be found at: http://www.winzip.com/wz7245.htm

## Disclosure Timeline

- 2006-08-28 - Vulnerability reported to vendor
- 2006-11-14 - Coordinated public release of advisory
