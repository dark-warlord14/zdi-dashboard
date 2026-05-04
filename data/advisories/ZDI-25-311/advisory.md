# ZDI-25-311: (Pwn2Own) Sonos Era 300 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-311
- **ZDI-CAN:** ZDI-CAN-25865
- **Date:** 2025-05-29
- **CVE:** CVE-2025-1051
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** Era 300
- **Credit:** Cody Gallagher and Charlie Waters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-311/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Sonos Era 300 speakers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of ALAC data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the anacapa user.

## Additional Details

Fixed in version Player v:83.1-61240 Release v:16.6

## Disclosure Timeline

- 2024-12-11 - Vulnerability reported to vendor
- 2025-05-29 - Coordinated public release of advisory
- 2025-05-29 - Advisory Updated
