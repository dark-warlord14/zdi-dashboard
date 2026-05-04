# ZDI-18-1405: Microsoft Office Excel XLS File Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1405
- **ZDI-CAN:** ZDI-CAN-6901
- **Date:** 2018-12-13
- **CVE:** CVE-2018-8598
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1405/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of Excel workbook files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8598

## Disclosure Timeline

- 2018-07-22 - Vulnerability reported to vendor
- 2018-12-13 - Coordinated public release of advisory
