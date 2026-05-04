# ZDI-21-813: Adobe Acrobat Reader DC setAction Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-813
- **ZDI-CAN:** ZDI-CAN-13855
- **Date:** 2021-07-15
- **CVE:** CVE-2021-28639
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Kc Udonsi (@glitchnsec) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-813/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the setAction method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-51.html

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
