# ZDI-18-1299: Advantech WebAccess Node drawsrv Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1299
- **ZDI-CAN:** ZDI-CAN-6286
- **Date:** 2018-10-24
- **CVE:** CVE-2018-14820
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1299/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2715 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this functionality to delete files under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-296-01

## Disclosure Timeline

- 2018-05-29 - Vulnerability reported to vendor
- 2018-10-24 - Coordinated public release of advisory
- 2018-10-24 - Advisory Updated
