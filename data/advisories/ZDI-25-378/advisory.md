# ZDI-25-378: (Pwn2Own) Ubiquiti Networks UniFi Console Missing Authentication for Critical Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-378
- **ZDI-CAN:** ZDI-CAN-25588
- **Date:** 2025-06-11
- **CVE:** CVE-2025-23116
- **CVSS:** 9.6
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** UniFi Console
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-378/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected Ubiquiti Networks UniFi Console devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of bridge device adoption requests. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication and disclose credentials for accessing connected devices.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-046-046/9649ea8f-93db-4713-a875-c3fd7614943f

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
