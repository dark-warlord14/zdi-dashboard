# ZDI-22-725: Adobe Photoshop Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-725
- **ZDI-CAN:** ZDI-CAN-17077
- **Date:** 2022-05-09
- **CVE:** CVE-2022-24099
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-725/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of embedded fonts. Crafted data in a font can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb22-20.html

## Disclosure Timeline

- 2022-04-13 - Vulnerability reported to vendor
- 2022-05-09 - Coordinated public release of advisory
