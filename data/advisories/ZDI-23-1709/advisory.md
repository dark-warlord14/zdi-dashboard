# ZDI-23-1709: Adobe Acrobat Reader DC AcroForm Doc Object Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1709
- **ZDI-CAN:** ZDI-CAN-22041
- **Date:** 2023-11-15
- **CVE:** CVE-2023-44361
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1709/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-54.html

## Disclosure Timeline

- 2023-08-31 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
