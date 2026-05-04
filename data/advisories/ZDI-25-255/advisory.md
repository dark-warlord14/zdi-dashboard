# ZDI-25-255: Allegra isZipEntryValide Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-255
- **ZDI-CAN:** ZDI-CAN-25730
- **Date:** 2025-04-24
- **CVE:** CVE-2025-3486
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** Mo0n Sha\xf0\x9d\x84\x9eow (VNPT Cyber Immunity)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Allegra. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the isZipEntryValide method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://alltena.com/en/resources/release-notes/release-notes-for-release-8-1-2

## Disclosure Timeline

- 2025-04-02 - Vulnerability reported to vendor
- 2025-04-24 - Coordinated public release of advisory
- 2025-04-24 - Advisory Updated
