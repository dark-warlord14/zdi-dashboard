# ZDI-18-1356: Microsoft Word doc File Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1356
- **ZDI-CAN:** ZDI-CAN-6706
- **Date:** 2018-11-21
- **CVE:** CVE-2018-8573
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Jaanus Kp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1356/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of .doc files. Crafted data in a .doc file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8573

## Disclosure Timeline

- 2018-07-10 - Vulnerability reported to vendor
- 2018-11-21 - Coordinated public release of advisory
