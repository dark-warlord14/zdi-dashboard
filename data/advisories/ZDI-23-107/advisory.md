# ZDI-23-107: (Pwn2Own) Ubiquiti Networks EdgeOS dhcp6c Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-107
- **ZDI-CAN:** ZDI-CAN-19687
- **Date:** 2023-02-09
- **CVE:** CVE-2023-23912
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** EdgeOS
- **Credit:** NCC Group EDG (@alexjplaskett @saidelike @FidgetingBits @_mccaulay)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-107/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Ubiquiti Networks EdgeOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dhcp6c daemon. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-028-028/696e4e3b-718c-4da4-9a21-965a85633b5f

## Disclosure Timeline

- 2022-12-22 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
