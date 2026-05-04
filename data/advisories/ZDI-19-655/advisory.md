# ZDI-19-655: Microsoft Excel Filename Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-655
- **ZDI-CAN:** ZDI-CAN-8524
- **Date:** 2019-07-10
- **CVE:** CVE-2019-1112
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** Jaanus Kp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-655/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process, which runs at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1112

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
