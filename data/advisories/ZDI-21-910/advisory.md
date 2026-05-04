# ZDI-21-910: Trend Micro Worry-Free Business Security Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-910
- **ZDI-CAN:** ZDI-CAN-12851
- **Date:** 2021-07-30
- **CVE:** CVE-2021-32464
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-910/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Worry-Free Business Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Worry-Free Business Services Agent. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000286857

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-07-30 - Coordinated public release of advisory
