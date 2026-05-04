# ZDI-19-702: Microsoft Windows JET Database Engine Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-702
- **ZDI-CAN:** ZDI-CAN-8277
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1147
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-702/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JET database engine. Crafted data in an MDB file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1147

## Disclosure Timeline

- 2019-04-16 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory
