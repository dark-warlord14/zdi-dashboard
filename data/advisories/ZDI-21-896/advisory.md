# ZDI-21-896: Adobe After Effects JPEG2000 Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-896
- **ZDI-CAN:** ZDI-CAN-13525
- **Date:** 2021-07-28
- **CVE:** CVE-2021-35994
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell (@mrpowell) & Joshua Smith (@kernelsmith) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-896/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of JPG2000 images. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb21-54.html

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-07-28 - Coordinated public release of advisory
