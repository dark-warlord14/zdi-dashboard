# ZDI-23-449: (Pwn2Own) Sonos One Speaker MPEG-TS Parser Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-449
- **ZDI-CAN:** ZDI-CAN-19773
- **Date:** 2023-04-14
- **CVE:** CVE-2023-27355
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** One Speaker
- **Credit:** Orange Tsai (@orange_8361) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-449/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Sonos One Speaker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MPEG-TS parser. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Sonos users with the S2 app installed should ensure their system is running software version 15.1 or later. Sonos users with the S1 app installed should be running version 11.7.1 or later. Users can check which software version they are running in the Sonos app > Settings > System > About My System. https://support.sonos.com/en-us/article/release-notes-for-sonos-s2

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-04-14 - Coordinated public release of advisory
- 2023-04-20 - Advisory Updated
