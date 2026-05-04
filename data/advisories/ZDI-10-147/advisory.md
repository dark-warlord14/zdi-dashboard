# ZDI-10-147: Microsoft Windows MPEG Layer-3 Audio Decoder Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-147
- **ZDI-CAN:** ZDI-CAN-698
- **Date:** 2010-08-10
- **CVE:** CVE-2010-1882
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows XP
- **Credit:** Moritz Jodeit of n.runs AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-147/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required in that a target must open a malicious media file or visit a malicious page. The specific flaw exists within the codec responsible for parsing layer 3 MPEG audio streams. By providing invalid values within the stream, heap memory can be easily corrupted. This could be leveraged by an attacker to execute remote code under the context of the user running the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS10-052.mspx

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2010-08-10 - Coordinated public release of advisory
