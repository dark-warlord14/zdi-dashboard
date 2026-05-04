# ZDI-19-649: Microsoft Windows gdiplus EMF Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-649
- **ZDI-CAN:** ZDI-CAN-8112
- **Date:** 2019-07-10
- **CVE:** CVE-2019-1102
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-649/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files in gdiplus.dll. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1102

## Disclosure Timeline

- 2019-03-27 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
