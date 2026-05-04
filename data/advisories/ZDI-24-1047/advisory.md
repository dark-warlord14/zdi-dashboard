# ZDI-24-1047: (0Day) ChargePoint Home Flex Bluetooth Low Energy Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1047
- **ZDI-CAN:** ZDI-CAN-21455
- **Date:** 2024-08-01
- **CVE:** CVE-2024-7392
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Todd Manning
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1047/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of ChargePoint Home Flex charging devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the connection handling of the Bluetooth Low Energy interface. The issue results from limiting the number of active connections to the product. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

11/13/23 – ZDI reported the vulnerability to the vendor. 04/29/24 – ZDI asked for an update. 05/24/24 – ZDI asked for an update. 05/29/24 – The vendor states that the vulnerability has been addressed but would need to get verification from QA. 07/22/24 – ZDI asked for an update. 07/29/24 – The ZDI informed the vendor that since we never received a confirmation that the vulnerability was patched, we have no choice but to assume this issue hasn’t been remediated and that we intend to publish the report as a zero-day advisory on 8/01/24.

## Disclosure Timeline

- 2023-11-13 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
