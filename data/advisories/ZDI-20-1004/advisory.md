# ZDI-20-1004: Microsoft Windows QuickTime Video Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1004
- **ZDI-CAN:** ZDI-CAN-10937
- **Date:** 2020-08-14
- **CVE:** CVE-2020-1492
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** @expend20
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of QuickTime videos in mfmp4srcsnk.dll. A crafted atom in a QuickTime video can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1492

## Disclosure Timeline

- 2020-05-07 - Vulnerability reported to vendor
- 2020-08-14 - Coordinated public release of advisory
