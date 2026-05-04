# ZDI-16-628: Advantech SUSIAccess Server downloadCSV file Parameter Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-628
- **ZDI-CAN:** ZDI-CAN-3831
- **Date:** 2016-12-13
- **CVE:** CVE-2016-9349
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** SUSIAccess Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-628/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech SUSIAccess Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of downloadCSV.jsp. When parsing the file element, the process fails to properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-336-04

## Disclosure Timeline

- 2016-08-17 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
