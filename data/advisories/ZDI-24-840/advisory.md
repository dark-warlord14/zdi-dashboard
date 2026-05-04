# ZDI-24-840: (Pwn2Own) Wyze Cam v3 TCP Traffic Handling Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-840
- **ZDI-CAN:** ZDI-CAN-22419
- **Date:** 2024-06-21
- **CVE:** CVE-2024-6249
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wyze
- **Affected Products:** Cam v3
- **Credit:** STEALIEN Inc. (Dohyun Kim, Sejun Oh, Hyeong Il Moon, Wonuk Bae, Jaehoon Jang, Bongeun Koo, Sungjun Park, Kitae Park, Wonbeen Im)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-840/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Wyze Cam v3 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TUTK P2P library. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Wyze has issued an update to correct this vulnerability. More details can be found at: https://forums.wyze.com/t/security-advisory/289256

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
