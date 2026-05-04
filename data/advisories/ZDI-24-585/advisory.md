# ZDI-24-585: Trend Micro VPN Proxy One Pro Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-585
- **ZDI-CAN:** ZDI-CAN-22715
- **Date:** 2024-06-10
- **CVE:** CVE-2024-36473
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** VPN Proxy One Pro
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-585/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro VPN Proxy One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Vpn Background Controller. By creating a symbolic link, an attacker can abuse the application to create a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-07247

## Disclosure Timeline

- 2024-01-28 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
