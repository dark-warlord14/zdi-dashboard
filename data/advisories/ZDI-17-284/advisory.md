# ZDI-17-284: Microsoft Windows ADO Array-Type Parameter Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-284
- **ZDI-CAN:** ZDI-CAN-4218
- **Date:** 2017-04-11
- **CVE:** CVE-2017-0158
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-284/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Microsoft ADO (ActiveX Data Objects) methods that accept an array as a parameter. By performing actions in script, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0158

## Disclosure Timeline

- 2016-11-30 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
