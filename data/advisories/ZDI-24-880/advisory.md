# ZDI-24-880: (Pwn2Own) Ubiquiti Networks EV Station EVCLauncher Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-880
- **ZDI-CAN:** ZDI-CAN-23187
- **Date:** 2024-06-21
- **CVE:** CVE-2024-29207
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** EV Station
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-880/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of Ubiquiti Networks EV Station. User interaction is not required to exploit this vulnerability. The specific flaw exists within the EVCLauncher application. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the application.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-bulletin-039-039/44e24007-2c2c-4ac0-bebf-3f19b9b24f09

## Disclosure Timeline

- 2024-02-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
