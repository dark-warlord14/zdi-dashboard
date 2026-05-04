# ZDI-22-146: Esri ArcReader PMF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-146
- **ZDI-CAN:** ZDI-CAN-14433
- **Date:** 2022-01-31
- **CVE:** CVE-2021-29117
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Esri
- **Affected Products:** ArcReader
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-146/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Esri ArcReader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PMF files. Crafted data in a PMF file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Esri has issued an update to correct this vulnerability. More details can be found at: https://www.esri.com/arcgis-blog/products/arcgis-desktop/administration/arcreader-general-data-frame-security-update/

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
