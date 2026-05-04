# ZDI-19-484: Adobe Acrobat Pro DC AcroForm XFA removeInstance Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-484
- **ZDI-CAN:** ZDI-CAN-7917
- **Date:** 2019-05-15
- **CVE:** CVE-2019-7760
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** peternguyen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-484/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AcroForm XFA removeInstance method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-18.html

## Disclosure Timeline

- 2019-02-07 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
