# ZDI-24-167: Adobe Acrobat Pro DC AcroForm Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-167
- **ZDI-CAN:** ZDI-CAN-22516
- **Date:** 2024-02-13
- **CVE:** CVE-2024-20734
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-167/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb24-07.html

## Disclosure Timeline

- 2023-12-11 - Vulnerability reported to vendor
- 2024-02-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
