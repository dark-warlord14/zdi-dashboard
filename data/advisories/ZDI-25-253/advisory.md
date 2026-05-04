# ZDI-25-253: SonicWALL Connect Tunnel Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-253
- **ZDI-CAN:** ZDI-CAN-25726
- **Date:** 2025-04-24
- **CVE:** CVE-2025-32817
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** Connect Tunnel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-253/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of SonicWALL Connect Tunnel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SonicWall VPN service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0007

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-04-24 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
