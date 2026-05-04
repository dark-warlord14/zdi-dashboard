# ZDI-21-136: Cisco Multiple Routers Cookie Header Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-136
- **ZDI-CAN:** ZDI-CAN-11726
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1293
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Multiple Routers
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-136/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV16x and RV26x routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv160-260-rce-XZeFkNHf

## Disclosure Timeline

- 2020-10-28 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
