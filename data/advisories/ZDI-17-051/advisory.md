# ZDI-17-051: Brocade Network Advisor SoftwareImageUpload Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-051
- **ZDI-CAN:** ZDI-CAN-4025
- **Date:** 2017-01-20
- **CVE:** CVE-2016-8206
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:C/A:C
- **Affected Vendors:** Brocade
- **Affected Products:** Network Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Brocade Network Advisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SoftwareImageUpload servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete arbitrary files under the context of SYSTEM.

## Additional Details

Brocade has issued an update to correct this vulnerability. More details can be found at: https://www.brocade.com/content/dam/common/documents/content-types/security-bulletin/brocade-security-advisory-2016-179.htm

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
