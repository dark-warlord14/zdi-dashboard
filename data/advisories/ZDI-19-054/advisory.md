# ZDI-19-054: Microsoft Office Word wwlib Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-054
- **ZDI-CAN:** ZDI-CAN-6838
- **Date:** 2019-01-17
- **CVE:** CVE-2019-0585
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Jaanus Kp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of DOC files in wwlib. A crafted file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0585

## Disclosure Timeline

- 2018-07-19 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
