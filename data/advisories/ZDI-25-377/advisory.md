# ZDI-25-377: (Pwn2Own) Ubiquiti Networks AI Bullet Improper Neutralization of Escape Sequences Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-377
- **ZDI-CAN:** ZDI-CAN-25603
- **Date:** 2025-06-11
- **CVE:** CVE-2025-23119
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** AI Bullet
- **Credit:** Bongeun Koo(@kiddo_pwn), Dohyun Kim(@d0now), Junyoung Choi(@insp3ct0r_x), Wonbeen Im(@D0b6y), Juhyeop Lee(@leeju_04), Juyeong Lee(@ju_cheda), GuckHyeon Jin(@nang__lam), Jongmin Kim(@slyfizz3) of STEALIEN Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-377/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected Ubiquiti Networks AI Bullet cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of DHCP packet options. The issue results from insufficient neutralization of special characters. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-046-046/9649ea8f-93db-4713-a875-c3fd7614943f

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
