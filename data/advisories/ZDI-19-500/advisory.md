# ZDI-19-500: Adobe Acrobat Reader DC removeField Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-500
- **ZDI-CAN:** ZDI-CAN-8180
- **Date:** 2019-05-15
- **CVE:** CVE-2019-7809
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** hemidallt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-500/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of field elements in AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-18.html

## Disclosure Timeline

- 2019-03-14 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
- 2020-08-18 - Advisory Updated
