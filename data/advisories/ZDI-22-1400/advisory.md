# ZDI-22-1400: Trend Micro Apex One Origin Validation Error Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1400
- **ZDI-CAN:** ZDI-CAN-17084
- **Date:** 2022-10-07
- **CVE:** CVE-2022-41749
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1400/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT Listener service. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000291645?language=en_US

## Disclosure Timeline

- 2022-04-06 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
