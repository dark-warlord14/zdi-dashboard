# ZDI-21-134: Cisco Multiple Routers RESTCONF file-upload Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-134
- **ZDI-CAN:** ZDI-CAN-11693
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1296
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Multiple Routers
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-134/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Cisco RV16x and RV26x routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv160-260-filewrite-7x9mnKjn

## Disclosure Timeline

- 2020-10-21 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
