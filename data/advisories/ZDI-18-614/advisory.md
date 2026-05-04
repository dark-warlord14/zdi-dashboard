# ZDI-18-614: Microsoft Windows WordPad Privilege Chaining Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-614
- **ZDI-CAN:** ZDI-CAN-5894
- **Date:** 2018-07-13
- **CVE:** CVE-2018-8307
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-614/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the fact that various operations can be triggered by a document in Microsoft WordPad. Considered individually, these operations do not pose a risk. However, they can be used in combination to produce an unsafe result. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8307

## Disclosure Timeline

- 2018-03-21 - Vulnerability reported to vendor
- 2018-07-13 - Coordinated public release of advisory
- 2018-07-13 - Advisory Updated
