# ZDI-23-1900: (0Day) BlueZ Audio Profile AVRCP Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1900
- **ZDI-CAN:** ZDI-CAN-19909
- **Date:** 2023-12-21
- **CVE:** CVE-2023-44431
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1900/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code via Bluetooth on affected installations of BlueZ. User interaction is required to exploit this vulnerability in that the target must connect to a malicious device. The specific flaw exists within the handling of the AVRCP protocol. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

07/26/23 – ZDI reported the vulnerability to the vendor 12/18/23 – ZDI asked for updates and notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-12-21 - Coordinated public release of advisory
- 2023-12-21 - Advisory Updated
