# ZDI-26-159: (Pwn2Own) Philips Hue Bridge hk_hap characteristics Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-159
- **ZDI-CAN:** ZDI-CAN-28479
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3561
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Philips
- **Affected Products:** Hue Bridge
- **Credit:** Thalium team from Thales Group (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-159/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of PUT requests to the characteristics endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in Bridge v2 Software version 1975170000 https://www.philips-hue.com/en-ca/support/release-notes/bridge

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
