# ZDI-23-661: (Pwn2Own) Synology RT6600ax Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-661
- **ZDI-CAN:** ZDI-CAN-19752
- **Date:** 2023-05-17
- **CVE:** CVE-2022-43932
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Rico Tubbing and Jurian van Dalfsen (Computest)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-661/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology RT6600ax routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the libsynoskd library. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_22_25

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
