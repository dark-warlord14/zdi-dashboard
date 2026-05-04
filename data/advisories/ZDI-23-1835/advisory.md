# ZDI-23-1835: Linux Mint Xreader EPUB File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1835
- **ZDI-CAN:** ZDI-CAN-21897
- **Date:** 2023-12-20
- **CVE:** CVE-2023-44451
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux Mint
- **Affected Products:** Xreader
- **Credit:** Febin Mon Saji
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1835/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Mint Xreader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EPUB files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Linux Mint has issued an update to correct this vulnerability. More details can be found at: https://github.com/linuxmint/xreader/commit/141f1313745b9cc73670df51ac145165efcbb14a

## Disclosure Timeline

- 2023-08-31 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
