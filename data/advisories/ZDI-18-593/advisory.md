# ZDI-18-593: Microsoft Office Excel Parsed Expression Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-593
- **ZDI-CAN:** ZDI-CAN-6340
- **Date:** 2018-06-26
- **CVE:** CVE-2018-8246
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-593/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of parsed expressions in FORMULA records in Excel workbooks. Crafted data can trigger access to memory prior to initialization. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8246

## Disclosure Timeline

- 2018-06-05 - Vulnerability reported to vendor
- 2018-06-26 - Coordinated public release of advisory
- 2018-06-26 - Advisory Updated
