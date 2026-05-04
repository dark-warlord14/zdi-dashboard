# ZDI-09-069: Microsoft Windows Media Player Audio Voice Sample Rate Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-069
- **ZDI-CAN:** ZDI-CAN-320
- **Date:** 2009-10-13
- **CVE:** CVE-2009-0555
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Windows Media Player 11, Windows Media Player 10
- **Credit:** Ivan Fratric
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. The specific flaw exists in the handling of Windows media audio files. When specifying a malicious sample rate for a Windows Media Voice frame, memory corruption can occur. Successful exploitation of this vulnerability can lead to remote compromise of the affected system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-051.mspx

## Disclosure Timeline

- 2008-04-16 - Vulnerability reported to vendor
- 2009-10-13 - Coordinated public release of advisory
