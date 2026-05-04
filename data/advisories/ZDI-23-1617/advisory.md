# ZDI-23-1617: Trend Micro Apex One Origin Validation Error Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1617
- **ZDI-CAN:** ZDI-CAN-21380
- **Date:** 2023-11-14
- **CVE:** CVE-2023-47196
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lays (@_L4ys) of TRAPA Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1617/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT Listener service. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000295652

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
