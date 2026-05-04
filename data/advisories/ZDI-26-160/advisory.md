# ZDI-26-160: (Pwn2Own) Philips Hue Bridge hk_hap Ed25519 Signature Verification Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-160
- **ZDI-CAN:** ZDI-CAN-28480
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3562
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Philips
- **Affected Products:** Hue Bridge
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-160/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ed25519_sign_open function. The issue results from improper verification of a cryptographic signature. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in Bridge v2 Software version 1975170000 https://www.philips-hue.com/en-ca/support/release-notes/bridge

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
