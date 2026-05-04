# ZDI-23-1155: SonicWALL GMS Virtual Appliance HttpDigestAuthenticator Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1155
- **ZDI-CAN:** ZDI-CAN-21221
- **Date:** 2023-08-21
- **CVE:** CVE-2023-34124
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** Alex Birnberg of Zymo Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1155/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SonicWALL GMS Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HttpDigestAuthenticator class. The issue results from a predictable digest credential in the authentication mechanism. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2023-0010

## Disclosure Timeline

- 2023-06-13 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
