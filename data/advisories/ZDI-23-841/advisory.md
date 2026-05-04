# ZDI-23-841: VMware Aria Operations for Networks getNotifiedEvents Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-841
- **ZDI-CAN:** ZDI-CAN-20612
- **Date:** 2023-06-08
- **CVE:** CVE-2023-20888
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Aria Operations for Networks
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-841/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware Aria Operations for Networks. Authentication is required to exploit this vulnerability. The specific flaw exists within the getNotifiedEvents method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of a service account that has unrestricted root privileges.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0012.html

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
