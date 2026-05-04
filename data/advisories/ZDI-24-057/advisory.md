# ZDI-24-057: Ivanti Avalanche SecureFilter Content-Type Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-057
- **ZDI-CAN:** ZDI-CAN-21943
- **Date:** 2024-01-11
- **CVE:** CVE-2023-46266
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-057/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SecureFilter class. The issue results from improper handling of the requested URI and accompanying Content-Type HTTP request header. An attacker can leverage this vulnerability to partially bypass authentication on the application.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-2-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2023-09-27 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
