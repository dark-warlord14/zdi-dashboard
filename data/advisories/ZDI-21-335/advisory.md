# ZDI-21-335: Adobe Acrobat Pro DC colorConvertPage Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-335
- **ZDI-CAN:** ZDI-CAN-12441
- **Date:** 2021-03-18
- **CVE:** CVE-2021-21088
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AIOFuzzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-335/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the colorConvertPage method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-09.html

## Disclosure Timeline

- 2020-12-09 - Vulnerability reported to vendor
- 2021-03-18 - Coordinated public release of advisory
