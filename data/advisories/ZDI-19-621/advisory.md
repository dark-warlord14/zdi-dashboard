# ZDI-19-621: Advantech WebAccess Node viewsrv Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-621
- **ZDI-CAN:** ZDI-CAN-8193
- **Date:** 2019-07-02
- **CVE:** CVE-2019-10983
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-621/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within viewsrv.dll, which is accessed through the 0x2722 IOCTL in the webvrpcs process. . The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-178-05

## Disclosure Timeline

- 2019-03-01 - Vulnerability reported to vendor
- 2019-07-02 - Coordinated public release of advisory
