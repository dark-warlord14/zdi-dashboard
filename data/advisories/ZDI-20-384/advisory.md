# ZDI-20-384: Advantech WebAccess/NMS download.jsp Directory Traversal Information Disclosure and Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-384
- **ZDI-CAN:** ZDI-CAN-9577
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10631
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-384/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information and delete arbitrary files on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the download.jsp endpoint. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM or to create a denial-of-service condition on the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
