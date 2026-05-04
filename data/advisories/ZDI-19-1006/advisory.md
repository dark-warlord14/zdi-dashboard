# ZDI-19-1006: Microsoft PowerPoint PPT File Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1006
- **ZDI-CAN:** ZDI-CAN-9339
- **Date:** 2019-12-11
- **CVE:** CVE-2019-1462
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PowerPoint
- **Credit:** Jaanus Kp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PowerPoint presentation files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1462

## Disclosure Timeline

- 2019-09-03 - Vulnerability reported to vendor
- 2019-12-11 - Coordinated public release of advisory
