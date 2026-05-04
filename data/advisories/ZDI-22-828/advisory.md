# ZDI-22-828: Adobe InCopy Font Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-828
- **ZDI-CAN:** ZDI-CAN-16453
- **Date:** 2022-06-15
- **CVE:** CVE-2022-30653
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** InCopy
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-828/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe InCopy. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of embedded fonts. Crafted data in a font can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/incopy/apsb22-29.html

## Disclosure Timeline

- 2022-02-04 - Vulnerability reported to vendor
- 2022-06-15 - Coordinated public release of advisory
