# ZDI-20-544: Cisco UCS Director saveWindowsNetworkConfig Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-544
- **ZDI-CAN:** ZDI-CAN-9604
- **Date:** 2020-04-16
- **CVE:** CVE-2020-3249
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** UCS Director
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-544/
## Vulnerability Details

This vulnerability allows remote attackers to overwrite arbitrary files on affected installations of Cisco UCS Director. Authentication is not required to exploit this vulnerability. The specific flaw exists within the saveWindowsNetworkConfig method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucsd-mult-vulns-UNfpdW4E

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
