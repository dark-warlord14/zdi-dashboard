# ZDI-21-581: Adobe Illustrator TTF Font Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-581
- **ZDI-CAN:** ZDI-CAN-12458
- **Date:** 2021-05-13
- **CVE:** CVE-2021-21101
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Illustrator
- **Credit:** Tran Van Khang \xe2\x80\x93 khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-581/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Illustrator. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of embedded fonts. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/illustrator/apsb21-24.html

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
