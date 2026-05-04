# ZDI-26-156: (Pwn2Own) Philips Hue Bridge HomeKit Accessory Protocol Transient Pairing Mode Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-156
- **ZDI-CAN:** ZDI-CAN-28374
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3558
- **CVSS:** 8.1
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Philips
- **Affected Products:** Hue Bridge
- **Credit:** Ho Xuan Ninh (@Xuanninh1412) and Hoang Hai Long (@seadragnol) from Qrious Secure (@qriousec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-156/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the HomeKit Accessory Protocol service, which listens on TCP port 8080 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in Bridge v2 Software version 1975170000 https://www.philips-hue.com/en-ca/support/release-notes/bridge

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
