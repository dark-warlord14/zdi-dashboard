# ZDI-17-947: Microsoft Windows VBScript VT_BSTR Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-947
- **ZDI-CAN:** ZDI-CAN-5243
- **Date:** 2017-12-12
- **CVE:** CVE-2017-11913
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-947/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of VT_BSTR string data in VBScript. By performing actions in VBScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11913

## Disclosure Timeline

- 2017-10-03 - Vulnerability reported to vendor
- 2017-12-12 - Coordinated public release of advisory
