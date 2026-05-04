# ZDI-25-251: (0Day) Harman Becker MGU21 Bluetooth Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-251
- **ZDI-CAN:** ZDI-CAN-23942
- **Date:** 2025-04-23
- **CVE:** CVE-2025-3885
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Harman Becker
- **Affected Products:** MGU21
- **Credit:** Aaron Luo, Gloria Chen, Omar Yang, Spencer Hsieh, and Vit Sembera of VicOne
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-251/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Harman Becker MGU21 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Bluetooth stack of the BCM89359 chipset. The issue results from the lack of proper validation of Bluetooth frames. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

06/12/24 – ZDI reported the vulnerability to the vendor 06/13/24 – the vendor acknowledged the receipt of the report 09/30/24 - ZDI asked for updates 10/01/24 – The vendor communicated that the reported behaviour will not be fixed by a third party 10/02/24 – ZDI informed the vendor of the intention to publish the case as a zero-day advisory

## Disclosure Timeline

- 2024-06-12 - Vulnerability reported to vendor
- 2025-04-23 - Coordinated public release of advisory
- 2025-04-23 - Advisory Updated
