# ZDI-25-380: Trend Micro Maximum Security Platinum Host Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-380
- **ZDI-CAN:** ZDI-CAN-25877
- **Date:** 2025-06-13
- **CVE:** CVE-2025-49385
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Vladislav Berghici of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-380/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Platinum Host Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-18461

## Disclosure Timeline

- 2024-12-06 - Vulnerability reported to vendor
- 2025-06-13 - Coordinated public release of advisory
- 2025-06-13 - Advisory Updated
