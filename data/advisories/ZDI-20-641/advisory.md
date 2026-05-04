# ZDI-20-641: Microsoft Windows PDF Library DirectWrite Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-641
- **ZDI-CAN:** ZDI-CAN-10381
- **Date:** 2020-05-12
- **CVE:** CVE-2020-1096
- **CVSS:** 9.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-641/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of Type1C fonts in the Windows PDF Library. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1096

## Disclosure Timeline

- 2020-02-10 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
