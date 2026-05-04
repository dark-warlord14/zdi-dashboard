# ZDI-24-1326: Ivanti Avalanche SecureFilter allowPassThrough Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1326
- **ZDI-CAN:** ZDI-CAN-23524
- **Date:** 2024-10-08
- **CVE:** CVE-2024-47010
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1326/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the allowPassThrough method. The issue results from incorrect string matching when making an authorization decision. An attacker can leverage this vulnerability to partially bypass authentication on the application.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Ivanti-Avalanche-6-4-5-Security-Advisory?language=en_US

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-10-08 - Coordinated public release of advisory
- 2024-10-08 - Advisory Updated
