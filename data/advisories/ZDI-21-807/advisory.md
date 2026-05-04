# ZDI-21-807: Adobe Acrobat Reader DC launchURL Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-807
- **ZDI-CAN:** ZDI-CAN-13550
- **Date:** 2021-07-15
- **CVE:** CVE-2021-35981
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Xu Peng from UCAS and Wang Yanhao from QiAnXin Technology Research Institute
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-807/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the launchURL method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-51.html

## Disclosure Timeline

- 2021-04-23 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
