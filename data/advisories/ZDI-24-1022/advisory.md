# ZDI-24-1022: Trend Micro VPN Proxy One Pro Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1022
- **ZDI-CAN:** ZDI-CAN-22716
- **Date:** 2024-07-30
- **CVE:** CVE-2024-41183
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** VPN Proxy One Pro
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1022/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro VPN Proxy One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VpnBackgroundController executable. By creating a symbolic link, an attacker can abuse the application to move arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-14460

## Disclosure Timeline

- 2024-03-06 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
