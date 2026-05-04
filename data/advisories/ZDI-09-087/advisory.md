# ZDI-09-087: Microsoft Internet Explorer CSS Race Condition Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-087
- **ZDI-CAN:** ZDI-CAN-541
- **Date:** 2009-12-08
- **CVE:** CVE-2009-3673
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Internet Explorer 8, Internet Explorer 7
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-087/
## Vulnerability Details

This vulnerability allows remote attackers to potentially execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during a race condition while repetitively clicking between two elements at a fast rate. When clicking back and forth between these two elements a corruption occurs resulting in a call to a dangling pointer which can be further leveraged into code execution via a heap spray. Exploitation of this vulnerability will lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-072.mspx

## Disclosure Timeline

- 2009-07-21 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory
