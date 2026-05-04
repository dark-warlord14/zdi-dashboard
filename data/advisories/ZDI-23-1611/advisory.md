# ZDI-23-1611: Trend Micro Apex One Security Agent Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1611
- **ZDI-CAN:** ZDI-CAN-20220
- **Date:** 2023-11-14
- **CVE:** CVE-2023-47192
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lays (@_L4ys) of TrapaSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1611/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT RealTime Scan service. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000295652

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
