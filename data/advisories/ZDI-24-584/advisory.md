# ZDI-24-584: (Pwn2Own) NETGEAR RAX30 fing_dil Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-584
- **ZDI-CAN:** ZDI-CAN-19843
- **Date:** 2024-06-10
- **CVE:** CVE-2023-51635
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Neodyme
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-584/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within fing_dil service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065928/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2023-0139

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
