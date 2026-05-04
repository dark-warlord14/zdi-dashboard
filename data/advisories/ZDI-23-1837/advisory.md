# ZDI-23-1837: Trimble SketchUp Viewer SKP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1837
- **ZDI-CAN:** ZDI-CAN-20789
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50187
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp Viewer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1837/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

fixed in windows version 23.2.101 and mac version 23.2.102

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
