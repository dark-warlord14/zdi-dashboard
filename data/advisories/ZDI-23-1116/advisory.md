# ZDI-23-1116: Ivanti Avalanche dumpHeap Incorrect Permission Assignment Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1116
- **ZDI-CAN:** ZDI-CAN-20904
- **Date:** 2023-08-15
- **CVE:** CVE-2023-32561
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1116/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dumpHeap method. The issue results from an incorrect permission assignment. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
