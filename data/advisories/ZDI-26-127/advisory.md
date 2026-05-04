# ZDI-26-127: (Pwn2Own) Ubiquiti Networks AI Pro Cleartext Transmission Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-127
- **ZDI-CAN:** ZDI-CAN-28474
- **Date:** 2026-02-25
- **CVE:** CVE-2026-21633
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** AI Pro
- **Credit:** David BERARD of @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-127/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Ubiquiti Networks AI Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within device authentication. The issue results from continuing to support a legacy authentication method. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-058-058/6922ff20-8cd7-4724-8d8c-676458a2d0f9

## Disclosure Timeline

- 2025-11-26 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
