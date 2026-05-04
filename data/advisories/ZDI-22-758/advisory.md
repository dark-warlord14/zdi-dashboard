# ZDI-22-758: (Pwn2Own) NETGEAR R6700v3 Vulnerable Third-Party Component Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-758
- **ZDI-CAN:** ZDI-CAN-15803
- **Date:** 2022-05-10
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Torchy's Corporate Ethical Hacking Team at crixer(@pwning_me), chillbro4201(@chillbro4201)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-758/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Netatalk library that is installed on NETGEAR R6700v3 routers. The issue results from the use of an outdated version of Netatalk containing known vulnerabilities. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064719/Security-Advisory-for-Multiple-Vulnerabilities-on-Multiple-Products-PSV-2021-0321

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
- 2022-05-11 - Advisory Updated
