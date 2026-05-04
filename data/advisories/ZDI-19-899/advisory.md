# ZDI-19-899: Adobe Acrobat Pro DC XFA closeDoc Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-899
- **ZDI-CAN:** ZDI-CAN-9331
- **Date:** 2019-10-15
- **CVE:** CVE-2019-8223
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Haikuo Xie of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-899/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the closeDoc method within XFA forms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-49.html

## Disclosure Timeline

- 2019-09-11 - Vulnerability reported to vendor
- 2019-10-15 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
