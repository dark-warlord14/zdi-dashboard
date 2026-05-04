# ZDI-18-161: Microsoft Office Excel Formula Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-161
- **ZDI-CAN:** ZDI-CAN-5325
- **Date:** 2018-02-21
- **CVE:** CVE-2018-0796
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-161/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of formulas in XLS files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0796

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
