# ZDI-24-543: (Pwn2Own) Sonos Era 100 SMB2 Message Handling Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-543
- **ZDI-CAN:** ZDI-CAN-22384
- **Date:** 2024-05-31
- **CVE:** CVE-2024-5267
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** Era 100
- **Credit:** @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-543/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Sonos Era 100 smart speakers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SMB2 messages. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Sonos users with the S2 app installed should ensure their system is running software version 16.0 or later. Users can check which software version they are running in the Sonos app > Settings > System > About My System. https://support.sonos.com/en-us/article/release-notes-for-sonos-s2

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
