# ZDI-22-1532: SAP 3D Visual Enterprise Viewer WRL File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1532
- **ZDI-CAN:** ZDI-CAN-18011
- **Date:** 2022-11-03
- **CVE:** CVE-2022-41196
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1532/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WRL files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://www.sap.com/documents/2022/02/fa865ea4-167e-0010-bca6-c68f7e60039b.html

## Disclosure Timeline

- 2022-07-22 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
