# ZDI-24-837: (Pwn2Own) Wyze Cam v3 Realtek Wi-Fi Driver Heap-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-837
- **ZDI-CAN:** ZDI-CAN-22310
- **Date:** 2024-06-21
- **CVE:** CVE-2024-6246
- **CVSS:** 9.6
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Wyze
- **Affected Products:** Cam v3
- **Credit:** Vincent DEHORS (@vdehors), Kevin DENIS (@0xmitsurugi), Romain KRAFT (@Areizen_) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-837/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Wyze Cam v3 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Realtek Wi-Fi kernel module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Wyze has issued an update to correct this vulnerability. More details can be found at: https://forums.wyze.com/t/security-advisory/289256

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
