# ZDI-21-135: Cisco Multiple Routers DNIAPI Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-135
- **ZDI-CAN:** ZDI-CAN-11716
- **Date:** 2021-02-04
- **CVE:** CVE-2021-1297
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Multiple Routers
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-135/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Cisco RV16x and RV26x routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv160-260-filewrite-7x9mnKjn

## Disclosure Timeline

- 2020-10-23 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
