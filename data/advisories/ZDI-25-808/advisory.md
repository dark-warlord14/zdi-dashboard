# ZDI-25-808: (0Day) AOMEI Cyber Backup Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-808
- **ZDI-CAN:** ZDI-CAN-26156
- **Date:** 2025-08-06
- **CVE:** CVE-2025-8610
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** AOMEI
- **Affected Products:** Cyber Backup
- **Credit:** Gu YongZeng (@0x0dee)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-808/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of AOMEI Cyber Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the StorageNode service, which listens on TCP port 9075 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

03/04/25 – ZDI contacted the vendor’s support team to request their PSIRT contacts 04/11/25 – ZDI asked for updates 07/29/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-07-29 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
