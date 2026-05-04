# ZDI-19-811: Microsoft Windows EMF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-811
- **ZDI-CAN:** ZDI-CAN-8729
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1252
- **CVSS:** 3.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-811/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1252

## Disclosure Timeline

- 2019-06-18 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
