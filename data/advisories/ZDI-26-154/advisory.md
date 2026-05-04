# ZDI-26-154: (Pwn2Own) Philips Hue Bridge HomeKit Pair-Setup Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-154
- **ZDI-CAN:** ZDI-CAN-28326
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3556
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Philips
- **Affected Products:** Hue Bridge
- **Credit:** InnoEdge Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-154/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the hk_hap_pair_storage_put function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the HomeKit service.

## Additional Details

Fixed in Bridge v2 Software version 1975170000 https://www.philips-hue.com/en-ca/support/release-notes/bridge

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
