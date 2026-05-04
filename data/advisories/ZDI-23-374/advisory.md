# ZDI-23-374: Microsoft 3D Builder WRL File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-374
- **ZDI-CAN:** ZDI-CAN-19006
- **Date:** 2023-03-31
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-374/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WRL files. Crafted data in a WRL file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft states this issue was fixed in the latest release as of February 7, 2023.

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
