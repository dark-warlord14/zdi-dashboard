# ZDI-20-249: Adobe Acrobat Reader DC Annotation Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-249
- **ZDI-CAN:** ZDI-CAN-9617
- **Date:** 2020-02-12
- **CVE:** CVE-2020-3748
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Xu Peng and Su Purui from TCA/SKLCS Institute of Software Chinese Academy of Sciences
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Annotation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-05.html

## Disclosure Timeline

- 2019-12-03 - Vulnerability reported to vendor
- 2020-02-12 - Coordinated public release of advisory
