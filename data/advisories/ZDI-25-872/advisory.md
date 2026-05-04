# ZDI-25-872: TeamViewer Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-872
- **ZDI-CAN:** ZDI-CAN-27129
- **Date:** 2025-08-26
- **CVE:** CVE-2025-44002
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** oriotie
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-872/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of TeamViewer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TeamViewer service. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2025-1003/

## Disclosure Timeline

- 2025-07-31 - Vulnerability reported to vendor
- 2025-08-26 - Coordinated public release of advisory
- 2025-08-26 - Advisory Updated
