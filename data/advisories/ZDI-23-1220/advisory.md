# ZDI-23-1220: (0Day) LG SuperSign Media Editor getSubFolderList Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1220
- **ZDI-CAN:** ZDI-CAN-20330
- **Date:** 2023-08-24
- **CVE:** CVE-2023-41181
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** LG
- **Affected Products:** SuperSign Media Editor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1220/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LG SuperSign Media Editor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getSubFolderList method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

03/10/23 – The ZDI reported the vulnerability to the vendor. 08/04/23 – The ZDI asked for an update. 08/08/23 – The vendor states that they do not have plans to fix the vulnerability now or in the future. 08/21/23 – The ZDI informed the vendor that we are publishing the case as a zero-day advisory on 08/24/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
