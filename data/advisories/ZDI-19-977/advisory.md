# ZDI-19-977: Microsoft Windows Kernel Type 1 Font Processing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-977
- **ZDI-CAN:** ZDI-CAN-9238
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1419
- **CVSS:** 8.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-977/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Type 1 fonts in the Windows kernel. A crafted font file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1419

## Disclosure Timeline

- 2019-08-07 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory
