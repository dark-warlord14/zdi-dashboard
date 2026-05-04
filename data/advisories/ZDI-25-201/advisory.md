# ZDI-25-201: Trend Micro Cleaner One Pro Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-201
- **ZDI-CAN:** ZDI-CAN-25572
- **Date:** 2025-04-07
- **CVE:** CVE-2025-27529
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:N/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Cleaner One Pro
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-201/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Cleaner One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additionally, the vulnerability is triggered only when an administrator performs an install of the product. The specific flaw exists within the product installer. By creating a symbolic link, an attacker can abuse the installer to create arbitrary files. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-09612

## Disclosure Timeline

- 2025-01-08 - Vulnerability reported to vendor
- 2025-04-07 - Coordinated public release of advisory
- 2025-04-07 - Advisory Updated
