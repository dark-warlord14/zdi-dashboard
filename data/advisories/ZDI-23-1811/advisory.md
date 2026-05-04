# ZDI-23-1811: BlueZ Phone Book Access Profile Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1811
- **ZDI-CAN:** ZDI-CAN-20936
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50229
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1811/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of BlueZ. User interaction is required to exploit this vulnerability in that the target must connect to a malicious Bluetooth device. The specific flaw exists within the handling of the Phone Book Access profile. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

BlueZ has issued an update to correct this vulnerability. More details can be found at: https://github.com/bluez/bluez/commit/5ab5352531a9cc7058cce569607f3a6831464443

## Disclosure Timeline

- 2023-04-26 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
