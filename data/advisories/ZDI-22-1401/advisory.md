# ZDI-22-1401: Trend Micro Apex One Security Agent Out-Of-Bounds Access Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1401
- **ZDI-CAN:** ZDI-CAN-17542
- **Date:** 2022-10-07
- **CVE:** CVE-2022-41745
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1401/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT Listener service. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000291645?language=en_US

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
