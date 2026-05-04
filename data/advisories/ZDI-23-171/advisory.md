# ZDI-23-171: Trend Micro Apex One Improper Access Control Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-171
- **ZDI-CAN:** ZDI-CAN-17686
- **Date:** 2023-02-24
- **CVE:** CVE-2023-25144
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-171/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One Security Agent. The specific flaw exists within the logic that controls access to the Suspect folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000292209

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2023-02-24 - Coordinated public release of advisory
