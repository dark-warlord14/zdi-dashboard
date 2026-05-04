# ZDI-21-1220: Trend Micro Apex One Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1220
- **ZDI-CAN:** ZDI-CAN-13846
- **Date:** 2021-10-19
- **CVE:** CVE-2021-42011
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Lays (@_L4ys)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1220/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ApexOne Security Agent. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289229

## Disclosure Timeline

- 2021-06-25 - Vulnerability reported to vendor
- 2021-10-19 - Coordinated public release of advisory
