# ZDI-23-371: Microsoft 3D Builder GLTF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-371
- **ZDI-CAN:** ZDI-CAN-19011
- **Date:** 2023-03-31
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-371/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLTF files. Crafted data in a GLTF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process at low integrity.

## Additional Details

Microsoft states this issue was fixed in the latest release as of March 10, 2023.

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
