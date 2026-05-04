# ZDI-21-171: Adobe Acrobat Reader DC Annots File ID Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-171
- **ZDI-CAN:** ZDI-CAN-12429
- **Date:** 2021-02-10
- **CVE:** CVE-2021-21042
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (@MarkYason)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-171/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the File ID parameter in the PDF trailer. By performing actions in JavaScript, an attacker can disclose the base address of Annots.api. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-09.html

## Disclosure Timeline

- 2020-12-09 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
