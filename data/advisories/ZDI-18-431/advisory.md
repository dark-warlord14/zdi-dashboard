# ZDI-18-431: Microsoft Office Excel Formula Record Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-431
- **ZDI-CAN:** ZDI-CAN-5725
- **Date:** 2018-05-14
- **CVE:** CVE-2018-8163
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-431/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of cell formula data in Excel worksheet files. Crafted data in a cell formula can trigger a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8163

## Disclosure Timeline

- 2018-03-08 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
