# ZDI-24-1046: (0Day) ChargePoint Home Flex Bluetooth Low Energy Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1046
- **ZDI-CAN:** ZDI-CAN-21454
- **Date:** 2024-08-01
- **CVE:** CVE-2024-7391
- **CVSS:** 2.6
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Todd Manning of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1046/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of ChargePoint Home Flex charging devices. User interaction is required to exploit this vulnerability. The specific flaw exists within the Wi-Fi setup logic. By connecting to the device over Bluetooth Low Energy during the setup process, an attacker can obtain Wi-Fi credentials. An attacker can leverage this vulnerability to disclose credentials and gain access to the device owner's Wi-Fi network.

## Additional Details

07/11/23 – ZDI reported the vulnerability to the vendor. 11/09/23 – ZDI asked for an update. 04/29/24 – ZDI asked for an update. 05/24/24 – ZDI asked for an update. 05/29/24 – The vendor states that the vulnerability has been addressed but would need to get verification from QA. 07/22/24 – ZDI asked for an update. 07/29/24 – The ZDI informed the vendor that since we never received a confirmation that the vulnerability was patched, we have no choice but to assume this issue hasn’t been remediated and that we intend to publish the report as a zero-day advisory on 8/01/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
