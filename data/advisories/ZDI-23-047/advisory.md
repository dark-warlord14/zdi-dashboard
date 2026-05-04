# ZDI-23-047: Microsoft 3D Builder GLTF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-047
- **ZDI-CAN:** ZDI-CAN-19125
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21792
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLTF files. Crafted data in a GLTF file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21792

## Disclosure Timeline

- 2022-10-13 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
