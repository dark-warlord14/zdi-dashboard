# ZDI-24-1335: SonicWALL Connect Tunnel Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1335
- **ZDI-CAN:** ZDI-CAN-22656
- **Date:** 2024-10-11
- **CVE:** CVE-2024-45315
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** Connect Tunnel
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1335/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of SonicWALL Connect Tunnel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SonicWall VPN. By creating a symbolic link, an attacker can abuse the application to create a file. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the host system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0017

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
