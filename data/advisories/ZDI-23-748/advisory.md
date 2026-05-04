# ZDI-23-748: SAP 3D Visual Enterprise Author DST File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-748
- **ZDI-CAN:** ZDI-CAN-18118
- **Date:** 2023-05-31
- **CVE:** CVE-2022-41211
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Author
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-748/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Author. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DST files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://d.dam.sap.com/a/3Hat4sC/2022%2012%20Patch%20Day%20Blog%20V9.0.pdf?rc=10

## Disclosure Timeline

- 2022-07-28 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
