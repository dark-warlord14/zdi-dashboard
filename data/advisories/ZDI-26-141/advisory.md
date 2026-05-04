# ZDI-26-141: Trend Micro Apex One Security Agent iCore Service Signature Verification Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-141
- **ZDI-CAN:** ZDI-CAN-26609
- **Date:** 2026-03-03
- **CVE:** CVE-2025-71215
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lays (@_L4ys) of TRAPA Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-141/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the iCore service. The issue results from the lack of proper file path checking during signature verification. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0022458

## Disclosure Timeline

- 2025-04-08 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
