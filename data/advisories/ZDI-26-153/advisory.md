# ZDI-26-153: (Pwn2Own) Philips Hue Bridge Zigbee Stack Custom Command Handler Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-153
- **ZDI-CAN:** ZDI-CAN-28276
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3555
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Philips
- **Affected Products:** Hue Bridge
- **Credit:** Mehdi Talbi, Matthieu Breuil, Théo Gordyjan from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-153/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. User interaction is required to exploit this vulnerability in that the user must initiate the device pairing process. The specific flaw exists within the handling of custom Zigbee ZCL frames in the Model Info download functionality. The issue results from the lack of proper validation of the size of data prior to copying it to a fixed-size heap buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in Bridge v2 Software version 1975170000 https://www.philips-hue.com/en-ca/support/release-notes/bridge

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
