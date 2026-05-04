# ZDI-22-853: Trend Micro Proxy One Pro Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-853
- **ZDI-CAN:** ZDI-CAN-16303
- **Date:** 2022-06-16
- **CVE:** CVE-2022-33158
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Proxy One Pro
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-853/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Proxy One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11042

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-06-16 - Coordinated public release of advisory
