# ZDI-18-952: Microsoft Office Word Preview Unsafe Hyperlink Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-952
- **ZDI-CAN:** ZDI-CAN-6284
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8316
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-952/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the display of Word documents in the preview pane in Windows Explorer. Crafted data in a Word file can result in a dangerous link being followed without first warning the user. An attacker can leverage this vulnerability to execute under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8316

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
