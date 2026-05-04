# ZDI-26-192: Sonos Era 300 SMB Response Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-192
- **ZDI-CAN:** ZDI-CAN-28345
- **Date:** 2026-03-16
- **CVE:** CVE-2026-4149
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** Era 300
- **Credit:** dmdung (@_piers2) of STAR Labs SG Pte. Ltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sonos Era 300. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the DataOffset field within SMB responses. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Fixed in version 83.1-61240 https://support.sonos.com/en-ca/article/release-notes-sonos-system-updates

## Disclosure Timeline

- 2025-11-06 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
