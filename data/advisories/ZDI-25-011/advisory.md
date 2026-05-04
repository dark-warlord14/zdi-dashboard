# ZDI-25-011: SonicWALL NSv Cryptographically Weak PRNG Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-011
- **ZDI-CAN:** ZDI-CAN-24818
- **Date:** 2025-01-09
- **CVE:** CVE-2024-40762
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** NSv
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar of Computest Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-011/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SonicWALL NSv. Authentication is not required to exploit this vulnerability. The specific flaw exists within the generation of cookies. The issue results from the use of a cryptographically weak pseudo-random number generator. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0003

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-01-09 - Coordinated public release of advisory
- 2025-01-09 - Advisory Updated
