# ZDI-24-1605: Adobe InDesign JP2 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1605
- **ZDI-CAN:** ZDI-CAN-24608
- **Date:** 2024-11-21
- **CVE:** CVE-2024-49529
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** InDesign
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1605/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe InDesign. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/indesign/apsb24-91.html

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-11-21 - Coordinated public release of advisory
- 2024-11-21 - Advisory Updated
