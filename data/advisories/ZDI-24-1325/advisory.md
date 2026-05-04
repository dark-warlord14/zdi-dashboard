# ZDI-24-1325: Ivanti Avalanche SecureFilter Content-Type Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1325
- **ZDI-CAN:** ZDI-CAN-23523
- **Date:** 2024-10-08
- **CVE:** CVE-2024-47009
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1325/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SecureFilter class. The issue results from improper handling of URIs and their accompanying Content-Type HTTP request headers. An attacker can leverage this vulnerability to partially bypass authentication on the application.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Ivanti-Avalanche-6-4-5-Security-Advisory?language=en_US

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-10-08 - Coordinated public release of advisory
- 2024-10-08 - Advisory Updated
