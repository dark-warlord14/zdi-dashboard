# ZDI-20-670: Adobe Premiere Rush MOV File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-670
- **ZDI-CAN:** ZDI-CAN-10871
- **Date:** 2020-05-25
- **CVE:** CVE-2020-9617
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Premiere Rush
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-670/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Premiere Rush. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MOV files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

https://helpx.adobe.com/security/products/premiere_rush/apsb20-29.html

## Disclosure Timeline

- 2020-04-09 - Vulnerability reported to vendor
- 2020-05-25 - Coordinated public release of advisory
