# ZDI-21-402: Trend Micro Apex One Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-402
- **ZDI-CAN:** ZDI-CAN-12147
- **Date:** 2021-04-12
- **CVE:** CVE-2021-28645
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Lays (@_L4ys)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-402/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ApexOne Security Agent. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000286019

## Disclosure Timeline

- 2020-12-11 - Vulnerability reported to vendor
- 2021-04-12 - Coordinated public release of advisory
