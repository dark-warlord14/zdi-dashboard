# ZDI-26-128: (Pwn2Own) Ubiquiti Networks AI Pro Uncaught Exception Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-128
- **ZDI-CAN:** ZDI-CAN-28824
- **Date:** 2026-02-25
- **CVE:** CVE-2026-21634
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** AI Pro
- **Credit:** David BERARD from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-128/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Ubiquiti Networks AI Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of WebSocket headers. The issue results from the lack of proper validation of user-supplied data, which can result in an uncaught exception. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-058-058/6922ff20-8cd7-4724-8d8c-676458a2d0f9

## Disclosure Timeline

- 2026-02-05 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
