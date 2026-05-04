# ZDI-23-1904: (0Day) BlueZ Audio Profile AVRCP parse_media_element Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1904
- **ZDI-CAN:** ZDI-CAN-20853
- **Date:** 2023-12-21
- **CVE:** CVE-2023-51589
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:L
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1904/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information via Bluetooth on affected installations of BlueZ. User interaction is required to exploit this vulnerability in that the target must connect to a malicious device. The specific flaw exists within the handling of the AVRCP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

07/04/23 – ZDI reported the vulnerabilities to the vendor 12/18/23 – ZDI asked for updates and notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-07 - Vulnerability reported to vendor
- 2023-12-21 - Coordinated public release of advisory
- 2023-12-21 - Advisory Updated
