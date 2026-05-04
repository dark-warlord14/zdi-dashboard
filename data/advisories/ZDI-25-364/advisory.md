# ZDI-25-364: Trend Micro Apex One Damage Cleanup Engine Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-364
- **ZDI-CAN:** ZDI-CAN-25273
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49157
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-364/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Damage Cleanup Engine, which runs within the Trend Micro Common Client Real-time Scan Service. By creating a junction, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019917

## Disclosure Timeline

- 2024-10-01 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
