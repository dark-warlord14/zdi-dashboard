# ZDI-23-1121: Ivanti Avalanche SecureFilter allowPassThrough Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1121
- **ZDI-CAN:** ZDI-CAN-21005
- **Date:** 2023-08-15
- **CVE:** CVE-2023-32566
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1121/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the allowPassThrough method. The issue results from incorrect string matching when making an authorization decision. An attacker can leverage this vulnerability to partially bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
