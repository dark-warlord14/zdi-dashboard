# ZDI-22-728: Microsoft Windows OpenType Font File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-728
- **ZDI-CAN:** ZDI-CAN-15915
- **Date:** 2022-05-10
- **CVE:** CVE-2022-26927
- **CVSS:** 9.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Uncodable
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-728/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OpenType font files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26927

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
