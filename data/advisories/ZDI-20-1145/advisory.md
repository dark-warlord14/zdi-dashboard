# ZDI-20-1145: SAP 3D Visual Enterprise Viewer SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1145
- **ZDI-CAN:** ZDI-CAN-11161
- **Date:** 2020-09-10
- **CVE:** CVE-2020-6334
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files within the sandbox subprocess. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=557449700

## Disclosure Timeline

- 2020-06-11 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
