# ZDI-10-016: Microsoft Windows ShellExecute Improper Sanitization Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-016
- **ZDI-CAN:** ZDI-CAN-495
- **Date:** 2010-02-09
- **CVE:** CVE-2010-0027
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows XP, Windows 2000, Windows Server 2003
- **Credit:** Brett Moore, Insomnia Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-016/
## Vulnerability Details

This vulnerability allows remote attackers to force a Microsoft Windows system to execute a given local executable. User interaction is required in that the target must access a malicious URL. The specific flaw exists within the ShellExecute API. Using a specially formatted URL an attacker can bypass sanitization checks within this function and force the calling application into running an executable of their choice. Successful exploitation requires a useful binary to exist in a predictable location on the remote system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-007.mspx

## Disclosure Timeline

- 2009-07-20 - Vulnerability reported to vendor
- 2010-02-09 - Coordinated public release of advisory
