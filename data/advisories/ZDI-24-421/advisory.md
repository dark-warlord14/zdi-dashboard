# ZDI-24-421: SonicWALL GMS Virtual Appliance ECMClientAuthenticator Hard-Coded Credential Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-421
- **ZDI-CAN:** ZDI-CAN-23521
- **Date:** 2024-05-07
- **CVE:** CVE-2024-29011
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** Erik Wynter
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-421/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SonicWALL GMS Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ECMClientAuthenticator class. The issue results from the use of a hard-coded credential. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0007

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-05-07 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
