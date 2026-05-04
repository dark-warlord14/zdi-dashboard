# ZDI-16-512: Microsoft Windows MSXML IDispatch Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-512
- **ZDI-CAN:** ZDI-CAN-3821
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3376
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-512/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within MSXML. By performing actions in script, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-116

## Disclosure Timeline

- 2016-06-06 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
