# ZDI-24-1511: Microsoft Office PowerPoint PPTX File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1511
- **ZDI-CAN:** ZDI-CAN-25090
- **Date:** 2024-11-14
- **CVE:** CVE-2024-49032
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1511/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PPTX files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49032

## Disclosure Timeline

- 2024-08-27 - Vulnerability reported to vendor
- 2024-11-14 - Coordinated public release of advisory
- 2024-11-14 - Advisory Updated
