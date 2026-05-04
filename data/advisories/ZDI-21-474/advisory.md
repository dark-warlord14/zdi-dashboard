# ZDI-21-474: Trend Micro HouseCall for Home Networks Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-474
- **ZDI-CAN:** ZDI-CAN-12552
- **Date:** 2021-04-23
- **CVE:** CVE-2021-28649
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** HouseCall for Home Networks
- **Credit:** Xavier Danest - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-474/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro HouseCall for Home Networks. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on product folders created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10310

## Disclosure Timeline

- 2021-01-08 - Vulnerability reported to vendor
- 2021-04-23 - Coordinated public release of advisory
