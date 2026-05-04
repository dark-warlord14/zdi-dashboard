# ZDI-23-710: (0Day) (Pwn2Own) Mikrotik RouterOS RADVD Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-710
- **ZDI-CAN:** ZDI-CAN-19797
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32154
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mikrotik
- **Affected Products:** RouterOS
- **Credit:** Angelboy(@scwuaptx) and NiNi (@terrynini38514) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-710/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Mikrotik RouterOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Router Advertisement Daemon. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

12/09/22 – ZDI reported the vulnerability to the vendor during Pwn2Own Toronto. 05/09/23 – ZDI asked for an update. 05/10/23 – The ZDI re-disclosed the report at the vendor’s request. 05/10/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 05/17/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
