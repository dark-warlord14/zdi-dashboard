# ZDI-20-379: Advantech WebAccess/NMS saveBackgroundAction Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-379
- **ZDI-CAN:** ZDI-CAN-9572
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10619
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-379/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitary files on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the saveBackground.action endpoint. When parsing the oldImage parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
