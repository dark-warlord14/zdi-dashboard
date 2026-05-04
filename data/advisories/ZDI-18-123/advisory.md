# ZDI-18-123: Microsoft Windows VBScript Filter Function Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-123
- **ZDI-CAN:** ZDI-CAN-5109
- **Date:** 2018-01-18
- **CVE:** CVE-2017-11887
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-123/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Filter function in VBScript. By performing actions in VBScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11887

## Disclosure Timeline

- 2017-09-01 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
