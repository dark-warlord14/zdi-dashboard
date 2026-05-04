# ZDI-22-677: Adobe Acrobat Pro DC AcroForm Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-677
- **ZDI-CAN:** ZDI-CAN-16349
- **Date:** 2022-04-28
- **CVE:** CVE-2022-27799
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Mark Vincent Yason (@MarkYason)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-677/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-16.html

## Disclosure Timeline

- 2022-02-04 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory
