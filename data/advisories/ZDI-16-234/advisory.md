# ZDI-16-234: Microsoft .NET Framework mscoreei DLL Planting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-234
- **ZDI-CAN:** ZDI-CAN-3578
- **Date:** 2016-04-12
- **CVE:** CVE-2016-0148
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET Framework
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-234/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft .NET Framework. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page or open a malicious directory or device. The specific flaw exists within the handling of a specific named DLL used by .NET Framework. By providing a directory with this specific DLL, an attacker is able to force the process to load an arbitrary DLL. This allows an attacker to execute arbitrary code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-041

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
