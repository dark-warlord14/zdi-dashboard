# ZDI-19-808: Microsoft Windows gdi32full Font Parsing Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-808
- **ZDI-CAN:** ZDI-CAN-8664
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1251
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-808/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of font files in the gdi32full library. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1251

## Disclosure Timeline

- 2019-06-04 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
