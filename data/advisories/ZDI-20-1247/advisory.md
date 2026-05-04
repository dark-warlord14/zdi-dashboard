# ZDI-20-1247: Microsoft 3D Builder GLB File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1247
- **ZDI-CAN:** ZDI-CAN-11174
- **Date:** 2020-10-19
- **CVE:** CVE-2020-1167
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1247/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-1167

## Disclosure Timeline

- 2020-06-04 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
