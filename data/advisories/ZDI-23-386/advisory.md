# ZDI-23-386: BlueZ Audio Profile AVRCP Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-386
- **ZDI-CAN:** ZDI-CAN-19908
- **Date:** 2023-04-12
- **CVE:** CVE-2023-27349
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** Michael Randrianantenaina (https://elkamika.blogspot.com/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-386/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code via Bluetooth on affected installations of BlueZ. User interaction is required to exploit this vulnerability in that the target must connect to a malicious device. The specific flaw exists within the handling of the AVRCP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

BlueZ has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/bluetooth/bluez.git/commit/?id=f54299a850676d92c3dafd83e9174fcfe420ccc9

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-04-12 - Coordinated public release of advisory
