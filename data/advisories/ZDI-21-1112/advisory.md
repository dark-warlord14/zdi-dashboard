# ZDI-21-1112: Trend Micro HouseCall for Home Networks Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1112
- **ZDI-CAN:** ZDI-CAN-13794
- **Date:** 2021-09-24
- **CVE:** CVE-2021-32466
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** HouseCall for Home Networks
- **Credit:** Xavier Danest - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1112/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro HouseCall for Home Networks. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-10626

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-09-24 - Coordinated public release of advisory
