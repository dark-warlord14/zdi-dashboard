# ZDI-18-056: Advantech WebAccess DelIcon Directory Traversal File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-056
- **ZDI-CAN:** ZDI-CAN-5058
- **Date:** 2018-01-05
- **CVE:** CVE-2017-16720
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-056/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DelIcon method in gmicons.asp. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files accessible to the web service.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-004-02

## Disclosure Timeline

- 2017-08-07 - Vulnerability reported to vendor
- 2018-01-05 - Coordinated public release of advisory
