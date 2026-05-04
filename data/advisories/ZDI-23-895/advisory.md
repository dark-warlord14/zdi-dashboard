# ZDI-23-895: TP-Link Tapo C210 Password Recovery Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-895
- **ZDI-CAN:** ZDI-CAN-20484
- **Date:** 2023-07-05
- **CVE:** CVE-2023-35717
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Tapo C210
- **Credit:** Cyrille Chatras
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-895/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of TP-Link Tapo C210 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the password recovery mechanism. The issue results from reliance upon the secrecy of the password derivation algorithm when generating a recovery password. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in firmware: 1.3.6 Build 230426 Rel.48373n https://www.tp-link.com/en/support/download/tapo-c210/#Firmware-Release-Notes

## Disclosure Timeline

- 2023-03-15 - Vulnerability reported to vendor
- 2023-07-05 - Coordinated public release of advisory
