# ZDI-23-887: Microsoft Windows PGM Invalid Transmission Group Size Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-887
- **ZDI-CAN:** ZDI-CAN-21089
- **Date:** 2023-06-16
- **CVE:** CVE-2023-29363
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Yazhi Wang from Trend Micro Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-887/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the Pragmatic General Multicast protocol. The issue results from the lack of proper validation of the Transmission Group Size field, which can result in corruption of an in-memory structure. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29363

## Disclosure Timeline

- 2023-06-01 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
