# ZDI-25-284: MATE Desktop Atril Document Viewer EPUB File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-284
- **ZDI-CAN:** ZDI-CAN-22063
- **Date:** 2025-05-02
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MATE Desktop
- **Affected Products:** Atril Document Viewer
- **Credit:** Febin Mon Saji
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-284/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MATE Desktop Atril Document Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EPUB files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in version 1.26.2 https://github.com/mate-desktop/atril/releases/tag/v1.26.2 https://github.com/mate-desktop/atril/commit/24f197791e9f666d2437a00229515c233b885821

## Disclosure Timeline

- 2025-03-12 - Vulnerability reported to vendor
- 2025-05-02 - Coordinated public release of advisory
- 2025-05-02 - Advisory Updated
