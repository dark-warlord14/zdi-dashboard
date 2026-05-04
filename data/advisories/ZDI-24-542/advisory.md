# ZDI-24-542: (Pwn2Own) Sonos Era 100 SMB2 Message Handling Integer Underflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-542
- **ZDI-CAN:** ZDI-CAN-22336
- **Date:** 2024-05-31
- **CVE:** CVE-2024-5256
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Sonos
- **Affected Products:** Era 100
- **Credit:** Interrupt Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-542/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Sonos Era 100 smart speakers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SMB2 messages. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Sonos users with the S2 app installed should ensure their system is running software version 16.0 or later. Users can check which software version they are running in the Sonos app > Settings > System > About My System. https://support.sonos.com/en-us/article/release-notes-for-sonos-s2

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
