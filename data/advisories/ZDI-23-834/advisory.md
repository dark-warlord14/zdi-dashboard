# ZDI-23-834: Trend Micro Apex One Security Agent Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-834
- **ZDI-CAN:** ZDI-CAN-19192
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34148
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Lays (@_L4ys)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-834/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT Listener service. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293322

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
