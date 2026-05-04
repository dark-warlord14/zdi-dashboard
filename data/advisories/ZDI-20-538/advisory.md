# ZDI-20-538: Cisco UCS Director downloadFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-538
- **ZDI-CAN:** ZDI-CAN-9557
- **Date:** 2020-04-16
- **CVE:** CVE-2020-3250
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** UCS Director
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-538/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco UCS Director. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the userAPIDownloadFile API, which calls the downloadFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose file contents in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucsd-mult-vulns-UNfpdW4E

## Disclosure Timeline

- 2019-12-20 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
