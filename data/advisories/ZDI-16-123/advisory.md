# ZDI-16-123: Advantech WebAccess Dashboard Viewer addFolder Directory Traversal Arbitrary File Deletion Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-123
- **ZDI-CAN:** ZDI-CAN-3131
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0855
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-123/
## Vulnerability Details

This vulnerability allows remote attackers to deny service to all users on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WebAccess Dashboard Viewer. Insufficient validation within the addFolder script allows unauthenticated callers to overwrite key system files so that access to the functionality of WebAccess is completely blocked to all users.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
