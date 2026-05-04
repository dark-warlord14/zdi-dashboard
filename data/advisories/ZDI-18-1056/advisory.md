# ZDI-18-1056: Microsoft Excel XLS File Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1056
- **ZDI-CAN:** ZDI-CAN-6389
- **Date:** 2018-09-14
- **CVE:** CVE-2018-8429
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1056/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of .xls files. Crafted data in an .xls file can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8429

## Disclosure Timeline

- 2018-06-19 - Vulnerability reported to vendor
- 2018-09-14 - Coordinated public release of advisory
- 2018-09-14 - Advisory Updated
