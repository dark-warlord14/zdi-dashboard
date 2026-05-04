# ZDI-21-130: Cisco Multiple Routers Authorization Header Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-130
- **ZDI-CAN:** ZDI-CAN-11686
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1289
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Multiple Routers
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-130/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV16x and RV26x routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. When parsing the Authorization header, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv160-260-rce-XZeFkNHf

## Disclosure Timeline

- 2020-10-16 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
