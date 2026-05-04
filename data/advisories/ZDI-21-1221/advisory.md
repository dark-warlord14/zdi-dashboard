# ZDI-21-1221: Trend Micro Worry-Free Business Security Stack-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1221
- **ZDI-CAN:** ZDI-CAN-13857
- **Date:** 2021-10-19
- **CVE:** CVE-2021-42012
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1221/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Worry-Free Business Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Security Server Database Service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289230

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-10-19 - Coordinated public release of advisory
