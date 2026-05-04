# ZDI-20-1094: Trend Micro Apex One Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1094
- **ZDI-CAN:** ZDI-CAN-10514
- **Date:** 2020-08-31
- **CVE:** CVE-2020-24557
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1094/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ApexOne Security Agent. The specific flaw exists within the logic that controls access to the Misc folder. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000263632

## Disclosure Timeline

- 2020-03-25 - Vulnerability reported to vendor
- 2020-08-31 - Coordinated public release of advisory
