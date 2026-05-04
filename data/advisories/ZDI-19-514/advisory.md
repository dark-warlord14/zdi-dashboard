# ZDI-19-514: Adobe Acrobat Pro DC JavaScript Annotation Object Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-514
- **ZDI-CAN:** ZDI-CAN-8437
- **Date:** 2019-05-15
- **CVE:** CVE-2019-7830
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Xu Peng and Su Purui from TCA/SKLCS Institute of Software Chinese Academy of Sciences
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-514/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Annotation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-18.html

## Disclosure Timeline

- 2019-04-04 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
