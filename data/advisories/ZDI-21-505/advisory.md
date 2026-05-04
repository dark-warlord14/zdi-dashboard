# ZDI-21-505: Esri ArcGIS Earth KMZ File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-505
- **ZDI-CAN:** ZDI-CAN-12462
- **Date:** 2021-05-03
- **CVE:** CVE-2021-29100
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Esri
- **Affected Products:** ArcGIS Earth
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-505/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Esri ArcGIS Earth. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of KMZ files. When handling filenames specified within a KMZ file, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Esri has issued an update to correct this vulnerability. More details can be found at: https://www.esri.com/arcgis-blog/products/arcgis-earth/administration/arcgis-earth-security-update/

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-05-03 - Coordinated public release of advisory
