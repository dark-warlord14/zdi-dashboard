# ZDI-25-989: Academy Software Foundation OpenEXR EXR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-989
- **ZDI-CAN:** ZDI-CAN-27946
- **Date:** 2025-11-11
- **CVE:** CVE-2025-12495
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Academy Software Foundation
- **Affected Products:** OpenEXR
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-989/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Academy Software Foundation OpenEXR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EXR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in OpenEXR v3.4.3 https://lists.aswf.io/g/openexr-dev/topic/openexr_v3_4_3_is_staged_for/116040425

## Disclosure Timeline

- 2025-09-25 - Vulnerability reported to vendor
- 2025-11-11 - Coordinated public release of advisory
- 2025-11-11 - Advisory Updated
