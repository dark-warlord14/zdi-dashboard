# ZDI-21-1249: Adobe Acrobat Reader DC AcroForm Field Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1249
- **ZDI-CAN:** ZDI-CAN-14484
- **Date:** 2021-10-28
- **CVE:** CVE-2021-40726
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mark Vincent Yason (@MarkYason)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForm fields. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-55.html

## Disclosure Timeline

- 2021-07-28 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
