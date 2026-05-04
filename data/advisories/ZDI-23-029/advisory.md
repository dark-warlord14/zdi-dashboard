# ZDI-23-029: Microsoft Print 3D PLY File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-029
- **ZDI-CAN:** ZDI-CAN-19022
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21782
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Print 3D
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Print 3D. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLY files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21782

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
