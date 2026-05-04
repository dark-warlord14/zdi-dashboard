# ZDI-22-1178: Trend Micro HouseCall Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1178
- **ZDI-CAN:** ZDI-CAN-16829
- **Date:** 2022-08-31
- **CVE:** CVE-2022-38764
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** HouseCall
- **Credit:** Xavier Danest - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1178/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro HouseCall. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on product folders created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11092

## Disclosure Timeline

- 2022-04-29 - Vulnerability reported to vendor
- 2022-08-31 - Coordinated public release of advisory
