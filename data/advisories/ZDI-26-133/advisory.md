# ZDI-26-133: (Pwn2Own) Music Assistant _update_library_item External Control of File Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-133
- **ZDI-CAN:** ZDI-CAN-28235
- **Date:** 2026-03-03
- **CVE:** CVE-2026-26975
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Music Assistant
- **Affected Products:** Music Assistant
- **Credit:** Emanuele Barbeno, Cyrill Bannwart, Urs Mueller, Lukasz D, Yves Bieri of Compass Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-133/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Music Assistant. Authentication is not required to exploit this vulnerability. The specific flaw exists within the _update_library_item method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Music Assistant has issued an update to correct this vulnerability. More details can be found at: https://github.com/music-assistant/server/security/advisories/GHSA-7jcc-p6xr-835j

## Disclosure Timeline

- 2025-11-05 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
