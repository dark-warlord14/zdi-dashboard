# ZDI-23-053: Trend Micro Maximum Security Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-053
- **ZDI-CAN:** ZDI-CAN-18291
- **Date:** 2023-01-18
- **CVE:** CVE-2022-48191
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-053/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Damage Cleanup Engine. The issue results from the lack of proper locking when performing file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11252

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
