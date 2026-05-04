# ZDI-23-1416: Microsoft 3D Builder GLB File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1416
- **ZDI-CAN:** ZDI-CAN-21073
- **Date:** 2023-09-12
- **CVE:** CVE-2023-36770
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1416/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLB files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36770

## Disclosure Timeline

- 2023-05-05 - Vulnerability reported to vendor
- 2023-09-12 - Coordinated public release of advisory
