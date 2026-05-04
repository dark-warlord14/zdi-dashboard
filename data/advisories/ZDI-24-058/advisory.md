# ZDI-24-058: Ivanti Avalanche SecureFilter allowPassThrough Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-058
- **ZDI-CAN:** ZDI-CAN-21953
- **Date:** 2024-01-11
- **CVE:** CVE-2021-22962
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-058/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the allowPassThrough method. The issue results from incorrect string matching when making an authorization decision. An attacker can leverage this vulnerability to partially bypass authentication on the application.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-2-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2023-09-27 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
