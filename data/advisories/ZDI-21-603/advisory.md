# ZDI-21-603: Trend Micro Maximum Security Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-603
- **ZDI-CAN:** ZDI-CAN-12346
- **Date:** 2021-05-21
- **CVE:** CVE-2021-32460
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-603/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Maximum Security console. The product sets incorrect permissions on a sensitive file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10336

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-05-21 - Coordinated public release of advisory
