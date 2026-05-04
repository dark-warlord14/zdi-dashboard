# ZDI-22-620: Trend Micro HouseCall for Home Networks Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-620
- **ZDI-CAN:** ZDI-CAN-16316
- **Date:** 2022-04-12
- **CVE:** CVE-2022-28339
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** HouseCall for Home Networks
- **Credit:** Xavier Danest - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-620/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro HouseCall for Home Networks. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the log4j scanner. The process loads a file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-21734

## Disclosure Timeline

- 2022-02-25 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
