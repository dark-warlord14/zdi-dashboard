# ZDI-24-1023: Trend Micro VPN Proxy One Pro Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1023
- **ZDI-CAN:** ZDI-CAN-22717
- **Date:** 2024-07-30
- **CVE:** CVE-2024-41183
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** VPN Proxy One Pro
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1023/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro VPN Proxy One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DEP Manager. By creating a symbolic link, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-14460

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
