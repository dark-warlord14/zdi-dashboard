# ZDI-25-379: (Pwn2Own) Ubiquiti Networks AI Bullet Insufficient Firmware Update Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-379
- **ZDI-CAN:** ZDI-CAN-25589
- **Date:** 2025-06-11
- **CVE:** CVE-2025-23117
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** AI Bullet
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-379/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Ubiquiti Networks AI Bullet Cameras. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of firmware updates. The issue results from the lack of proper validation of firmware update packages. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-046-046/9649ea8f-93db-4713-a875-c3fd7614943f

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
