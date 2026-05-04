# ZDI-22-990: Adobe Acrobat Reader DC Font Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-990
- **ZDI-CAN:** ZDI-CAN-16952
- **Date:** 2022-07-13
- **CVE:** CVE-2022-34217
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-990/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of embedded fonts. Crafted data in a font file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-32.html

## Disclosure Timeline

- 2022-04-01 - Vulnerability reported to vendor
- 2022-07-13 - Coordinated public release of advisory
