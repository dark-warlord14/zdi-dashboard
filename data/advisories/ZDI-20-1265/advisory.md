# ZDI-20-1265: SAP 3D Visual Enterprise Viewer SVG File XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1265
- **ZDI-CAN:** ZDI-CAN-11243
- **Date:** 2020-10-19
- **CVE:** CVE-2020-6315
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1265/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of SVG files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Fixed in version 9.0 FP09 MP3

## Disclosure Timeline

- 2020-08-28 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
