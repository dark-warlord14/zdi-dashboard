# ZDI-20-1134: Microsoft Windows WebM Video Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1134
- **ZDI-CAN:** ZDI-CAN-11511
- **Date:** 2020-09-10
- **CVE:** CVE-2020-1319
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Wen guang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WebM videos. Crafted data in a WebM video can trigger access to a pointer prior to initialization. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1319

## Disclosure Timeline

- 2020-07-29 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
