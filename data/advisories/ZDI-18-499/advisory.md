# ZDI-18-499: Advantech WebAccess Node webvrpcs drawsrv Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-499
- **ZDI-CAN:** ZDI-CAN-5664
- **Date:** 2018-05-18
- **CVE:** CVE-2018-7495
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-499/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2715 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this functionality to delete files under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-02-09 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
