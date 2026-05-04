# ZDI-18-298: Microsoft Windows JScript defineProperty Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-298
- **ZDI-CAN:** ZDI-CAN-5769
- **Date:** 2018-04-11
- **CVE:** CVE-2018-0987
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-298/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows JScript. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the defineProperty method. By performing actions in JScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0987

## Disclosure Timeline

- 2018-03-08 - Vulnerability reported to vendor
- 2018-04-11 - Coordinated public release of advisory
- 2018-04-11 - Advisory Updated
