# ZDI-23-835: Trend Micro Apex One Security Agent Untrusted Search Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-835
- **ZDI-CAN:** ZDI-CAN-19680
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34144
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Lays (@_L4ys)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-835/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One Client Plug-in Service Manager. The issue results from loading a module from an untrusted location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293322

## Disclosure Timeline

- 2022-12-22 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
