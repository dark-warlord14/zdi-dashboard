# ZDI-25-179: (0Day) CarlinKit CPC200-CCPA Improper Verification of Cryptographic Signature Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-179
- **ZDI-CAN:** ZDI-CAN-24356
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2763
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** CarlinKit
- **Affected Products:** CPC200-CCPA
- **Credit:** (VicOne Inc) Aaron Luo, Spencer Hsieh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-179/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of CarlinKit CPC200-CCPA devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of update packages on USB drives. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

06/05/24 – ZDI contacted the vendor’s support team via email 07/12/24 – ZDI sent a second PSIRT contact request to CarlinKit support team 11/13/24 – ZDI asked for updates 02/18/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
