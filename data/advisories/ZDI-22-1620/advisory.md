# ZDI-22-1620: Trend Micro Apex One Security Agent Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1620
- **ZDI-CAN:** ZDI-CAN-17337
- **Date:** 2022-11-21
- **CVE:** CVE-2022-44651
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1620/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One Client Plug-in Service Manager. The issue results from the lack of proper locking when performing operations on a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000291770

## Disclosure Timeline

- 2022-07-22 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
