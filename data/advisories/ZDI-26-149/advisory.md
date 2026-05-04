# ZDI-26-149: Trend Micro Cleaner One Pro Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-149
- **ZDI-CAN:** ZDI-CAN-28218
- **Date:** 2026-03-03
- **CVE:** CVE-2025-71218
- **CVSS:** 5.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Cleaner One Pro
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-149/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Cleaner One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. By creating a symbolic link, an attacker can abuse the installer to create an arbitrary file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-13129

## Disclosure Timeline

- 2025-12-24 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
