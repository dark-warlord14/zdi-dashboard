# ZDI-22-260: (Pwn2Own) Sonos One Speaker Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-260
- **ZDI-CAN:** ZDI-CAN-15828
- **Date:** 2022-02-14
- **CVE:** CVE-2022-24046
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** One Speaker
- **Credit:** Orange Tsai (@orange_8361) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-260/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Sonos One Speaker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the anacapd daemon. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in S2 software version 13.4.1 or later and S1 software version 11.2.13 build 57923290 or later.

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-02-14 - Coordinated public release of advisory
- 2022-12-09 - Advisory Updated
