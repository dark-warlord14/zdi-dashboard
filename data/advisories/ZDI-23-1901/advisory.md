# ZDI-23-1901: (0Day) BlueZ OBEX Library Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1901
- **ZDI-CAN:** ZDI-CAN-20937
- **Date:** 2023-12-21
- **CVE:** CVE-2023-51594
- **CVSS:** 2.6
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1901/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of BlueZ. User interaction is required to exploit this vulnerability in that the target must connect to a malicious Bluetooth device. The specific flaw exists within the handling of OBEX protocol parameters. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

07/26/23 – ZDI reported the vulnerability to the vendor 12/18/23 – ZDI asked for updates and notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-26 - Vulnerability reported to vendor
- 2023-12-21 - Coordinated public release of advisory
- 2023-12-21 - Advisory Updated
