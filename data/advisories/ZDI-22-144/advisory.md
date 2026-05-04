# ZDI-22-144: Esri ArcReader PMF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-144
- **ZDI-CAN:** ZDI-CAN-14267
- **Date:** 2022-01-31
- **CVE:** CVE-2021-29112
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Esri
- **Affected Products:** ArcReader
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-144/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Esri ArcReader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PMF files. Crafted data in a PMF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Esri has issued an update to correct this vulnerability. More details can be found at: https://www.esri.com/arcgis-blog/products/arcgis-desktop/administration/arcreader-general-data-frame-security-update/

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
