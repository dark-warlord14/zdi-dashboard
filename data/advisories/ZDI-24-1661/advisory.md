# ZDI-24-1661: Veritas Enterprise Vault HTMLView Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1661
- **ZDI-CAN:** ZDI-CAN-24696
- **Date:** 2024-12-11
- **CVE:** CVE-2024-52942
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Veritas
- **Affected Products:** Enterprise Vault
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1661/
## Vulnerability Details

This vulnerability allows remote attackers to execute web requests with the target user's privileges on affected installations of Veritas Enterprise Vault. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the HTMLView endpoint. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to interact with the application in the context of the target user.

## Additional Details

Veritas has issued an update to correct this vulnerability. More details can be found at: https://www.veritas.com/support/en_US/security/VTS24-013

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
