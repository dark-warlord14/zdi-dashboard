# ZDI-26-126: (Pwn2Own) Ubiquiti Networks AI Pro Discovery Protocol Missing Encryption Protocol Downgrade Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-126
- **ZDI-CAN:** ZDI-CAN-28274
- **Date:** 2026-02-25
- **CVE:** CVE-2026-21633
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** AI Pro
- **Credit:** David BERARD from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-126/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to downgrade the communication protocol on affected installations of Ubiquiti Networks AI Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the discovery protocol. The issue results from the lack of encryption in the communications channel. An attacker can leverage this vulnerability to downgrade the communication protocol used by the system.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-058-058/6922ff20-8cd7-4724-8d8c-676458a2d0f9

## Disclosure Timeline

- 2025-11-26 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
