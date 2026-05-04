# ZDI-25-224: (Pwn2Own) Sonos Era 300 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-224
- **ZDI-CAN:** ZDI-CAN-25601
- **Date:** 2025-04-09
- **CVE:** CVE-2025-1049
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** Era 300
- **Credit:** InfoSect
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-224/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Sonos Era 300 speakers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of ID3 data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the anacapa user.

## Additional Details

Sonos users should ensure their system is running the appropriate software version. For the Sonos app this is version 16.6 or later: go to Settings > General Settings > About My System to check the version. For the Sonos S1 app this is version 11.15.1 or later: go to More > Settings > System Updates > System Info to check the version. Sonos Security Advisory: https://www.sonos.com/en-us/security-advisory-2024-0002 Update instructions: https://support.sonos.com/en-us/article/update-your-sonos-speakers

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
