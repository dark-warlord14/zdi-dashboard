# ZDI-23-973: (Pwn2Own) Tesla Model 3 bsa_server BIP Heap-based Buffer Overflow Arbitrary Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-973
- **ZDI-CAN:** ZDI-CAN-20737
- **Date:** 2023-07-18
- **CVE:** CVE-2023-32157
- **CVSS:** 4.6
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** David BERARD (@_p0ly_) and Vincent DEHORS (@vdehors) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-973/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Tesla Model 3 vehicles. An attacker must first obtain the ability to pair a malicious Bluetooth device with the target system in order to exploit this vulnerability. The specific flaw exists within the bsa_server process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of an unprivileged user in a sandboxed process.

## Additional Details

Fixed in 2023.20 firmware release.

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-07-18 - Coordinated public release of advisory
