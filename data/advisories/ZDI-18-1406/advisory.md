# ZDI-18-1406: Microsoft Office PowerPoint PPT File Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1406
- **ZDI-CAN:** ZDI-CAN-6745
- **Date:** 2018-12-13
- **CVE:** CVE-2018-8628
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Jaanus Kp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1406/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PowerPoint presentation files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8628

## Disclosure Timeline

- 2018-07-15 - Vulnerability reported to vendor
- 2018-12-13 - Coordinated public release of advisory
