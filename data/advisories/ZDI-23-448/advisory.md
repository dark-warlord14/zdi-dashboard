# ZDI-23-448: (Pwn2Own) Sonos One Speaker msprox Endpoint Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-448
- **ZDI-CAN:** ZDI-CAN-19846
- **Date:** 2023-04-14
- **CVE:** CVE-2023-27353
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Sonos
- **Affected Products:** One Speaker
- **Credit:** Phan Thanh Duy (@PTDuy) & Nguyen Hoang Thach (@hi_im_d4rkn3ss) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-448/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Sonos One Speaker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the msprox endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Sonos users with the S2 app installed should ensure their system is running software version 15.1 or later. Sonos users with the S1 app installed should be running version 11.7.1 or later. Users can check which software version they are running in the Sonos app > Settings > System > About My System. https://support.sonos.com/en-us/article/release-notes-for-sonos-s2

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-04-14 - Coordinated public release of advisory
