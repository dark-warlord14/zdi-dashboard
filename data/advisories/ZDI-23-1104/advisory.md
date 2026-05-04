# ZDI-23-1104: Fortinet FortiClient VPN Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1104
- **ZDI-CAN:** ZDI-CAN-18590
- **Date:** 2023-08-14
- **CVE:** CVE-2022-43946
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiClient VPN
- **Credit:** Ting
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiClient VPN. Authentication is required to exploit this vulnerability. The specific flaw exists within the FortiClient Logging daemon. The product applies insufficient access controls to a sensitive pipe. A remote attacker can leverage this vulnerability to execute code in the context of SYSTEM. Additionally, a local attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-22-429

## Disclosure Timeline

- 2022-10-31 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory
