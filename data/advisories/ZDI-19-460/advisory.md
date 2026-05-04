# ZDI-19-460: Microsoft Office PowerPoint gdiplus ConvertToEmfPlus Untrusted Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-460
- **ZDI-CAN:** ZDI-CAN-7670
- **Date:** 2019-05-15
- **CVE:** CVE-2019-0882
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** willJ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-460/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ConvertToEmfPlus function in gdiplus. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0882

## Disclosure Timeline

- 2019-01-23 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
