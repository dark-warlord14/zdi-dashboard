# ZDI-22-017: Trend Micro Apex One Origin Validation Error Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-017
- **ZDI-CAN:** ZDI-CAN-14607
- **Date:** 2022-01-06
- **CVE:** CVE-2021-45441
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lays (@_L4ys) of TrapaSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-017/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT RealTime Scan service. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289996

## Disclosure Timeline

- 2021-08-27 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
