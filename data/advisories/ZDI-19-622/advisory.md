# ZDI-19-622: Advantech WebAccess Node viewsrv Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-622
- **ZDI-CAN:** ZDI-CAN-8194
- **Date:** 2019-07-02
- **CVE:** CVE-2019-10985
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-622/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2715 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-178-05

## Disclosure Timeline

- 2019-03-01 - Vulnerability reported to vendor
- 2019-07-02 - Coordinated public release of advisory
