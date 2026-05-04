# ZDI-16-126: Advantech WebAccess Dashboard Viewer openWidget Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-126
- **ZDI-CAN:** ZDI-CAN-3133
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0855
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** kimiya & rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-126/
## Vulnerability Details

This vulnerability allows remote attackers to disclose arbitrary file contents on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WebAccess Dashboard Viewer. Insufficient validation within the openWidget script allows unauthenticated callers to read the content of arbitrary files on the WebAccess server.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
