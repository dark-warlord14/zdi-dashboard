# ZDI-26-080: Ivanti Endpoint Manager AuthHelper Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-080
- **ZDI-CAN:** ZDI-CAN-26885
- **Date:** 2026-02-12
- **CVE:** CVE-2026-1603
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-080/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AuthHelper class. The issue results from using an alternative, weak authentication path. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://hub.ivanti.com/s/article/Security-Advisory-EPM-February-2026-for-EPM-2024?language=en_US

## Disclosure Timeline

- 2025-11-25 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
