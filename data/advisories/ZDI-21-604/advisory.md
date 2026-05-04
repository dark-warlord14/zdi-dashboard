# ZDI-21-604: Dräger X-dock Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-604
- **ZDI-CAN:** ZDI-CAN-11783
- **Date:** 2021-05-21
- **CVE:** CVE-2021-28111
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dräger
- **Affected Products:** X-dock
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-604/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dr��ger X-dock. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware and filesystem of the display. The firmware and filesystem contain hard-coded default credentials. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Dräger has issued an update to correct this vulnerability. More details can be found at: https://static.draeger.com/security/download/PSA-21-120-1-X-Dock-Product-Security-Advisory.pdf

## Disclosure Timeline

- 2021-01-19 - Vulnerability reported to vendor
- 2021-05-21 - Coordinated public release of advisory
