# ZDI-21-372: Esri ArcReader PMF File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-372
- **ZDI-CAN:** ZDI-CAN-12596
- **Date:** 2021-03-30
- **CVE:** CVE-2021-29098
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Esri
- **Affected Products:** ArcReader
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-372/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Esri ArcReader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PMF files. Crafted data in a PMF file can trigger access to a pointer prior to initialization. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Esri has issued an update to correct this vulnerability. More details can be found at: https://www.esri.com/arcgis-blog/products/arcgis/administration/security-advisory-general-raster

## Disclosure Timeline

- 2020-12-09 - Vulnerability reported to vendor
- 2021-03-30 - Coordinated public release of advisory
