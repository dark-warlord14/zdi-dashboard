# ZDI-20-937: NETGEAR Multiple Routers check_ra Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-937
- **ZDI-CAN:** ZDI-CAN-9852
- **Date:** 2020-08-04
- **CVE:** CVE-2020-15636
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) and Radek Domanski (@RabbitPro | radek.domanski@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-937/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR R6400, R6700, R7000, R7850, R7900, R8000, RS400, and XR300 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the check_ra service. A crafted raePolicyVersion in a RAE_Policy.json file can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062128/Security-Advisory-for-Pre-Authentication-Stack-Overflow-on-R6700v3-PSV-2020-0224

## Disclosure Timeline

- 2020-05-13 - Vulnerability reported to vendor
- 2020-08-04 - Coordinated public release of advisory
