# ZDI-22-068: Adobe InDesign JPEG File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-068
- **ZDI-CAN:** ZDI-CAN-15232
- **Date:** 2022-01-13
- **CVE:** CVE-2021-45058
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** InDesign
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe InDesign. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG images. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/indesign/apsb22-05.html

## Disclosure Timeline

- 2021-09-15 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
