# ZDI-17-322: Advantech WebAccess odbcPg4 Absolute Path Traversal File Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-322
- **ZDI-CAN:** ZDI-CAN-4013
- **Date:** 2017-05-04
- **CVE:** CVE-2017-7929
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-322/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service condition on vulnerable installations of Advantech WebAccess. Authentication is required to exploit this vulnerability. The specific flaw exists within odbcPg4.asp. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to overwrite key web files which will disable functionality on the target machine.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-124-03

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-05-04 - Coordinated public release of advisory
