# ZDI-25-834: Academy Software Foundation OpenEXR EXR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-834
- **ZDI-CAN:** ZDI-CAN-26141
- **Date:** 2025-08-13
- **CVE:** CVE-2025-48071
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Academy Software Foundation
- **Affected Products:** OpenEXR
- **Credit:** Dongjun Kim(@Enki WhiteHat) and Jongseong Kim(@Enki Whitehat)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-834/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Academy Software Foundation OpenEXR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EXR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Academy Software Foundation has issued an update to correct this vulnerability. More details can be found at: https://github.com/AcademySoftwareFoundation/openexr/security/advisories/GHSA-h45x-qhg2-q375

## Disclosure Timeline

- 2025-03-18 - Vulnerability reported to vendor
- 2025-08-13 - Coordinated public release of advisory
- 2025-08-13 - Advisory Updated
