# ZDI-22-1619: Trend Micro Apex One Unauthorized Change Prevention Service Out-Of-Bounds Access Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1619
- **ZDI-CAN:** ZDI-CAN-17387
- **Date:** 2022-11-21
- **CVE:** CVE-2022-44649
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1619/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Unauthorized Change Prevention Service. A crafted request can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000291770

## Disclosure Timeline

- 2022-05-10 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
