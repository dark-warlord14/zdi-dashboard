# ZDI-24-879: (Pwn2Own) Ubiquiti Networks EV Station changeUserPassword Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-879
- **ZDI-CAN:** ZDI-CAN-23186
- **Date:** 2024-06-21
- **CVE:** CVE-2024-29208
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** EV Station
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-879/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Ubiquiti Networks EV Station. Authentication is not required to exploit this vulnerability. The specific flaw exists within the password change functionality. The issue results from the lack of proper validation of the old password before setting a new password. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-bulletin-039-039/44e24007-2c2c-4ac0-bebf-3f19b9b24f09

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
