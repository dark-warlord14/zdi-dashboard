# ZDI-20-543: Cisco UCS Director saveStaticConfig Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-543
- **ZDI-CAN:** ZDI-CAN-9596
- **Date:** 2020-04-16
- **CVE:** CVE-2020-3248
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** UCS Director
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-543/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco UCS Director. Authentication is not required to exploit this vulnerability. The specific flaw exists within the saveStaticConfig method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucsd-mult-vulns-UNfpdW4E

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
