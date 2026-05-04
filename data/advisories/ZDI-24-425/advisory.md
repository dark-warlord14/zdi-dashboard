# ZDI-24-425: Adobe Acrobat Reader DC AcroForm Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-425
- **ZDI-CAN:** ZDI-CAN-23044
- **Date:** 2024-05-07
- **CVE:** CVE-2024-30303
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (markyason.github.io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-425/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb24-07.html

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-05-07 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
