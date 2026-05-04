# ZDI-20-1378: Trend Micro ServerProtect ioctlMod Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1378
- **ZDI-CAN:** ZDI-CAN-11064
- **Date:** 2020-11-24
- **CVE:** CVE-2020-28575
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1378/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro ServerProtect. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ioctlMod function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000281950

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-11-24 - Coordinated public release of advisory
