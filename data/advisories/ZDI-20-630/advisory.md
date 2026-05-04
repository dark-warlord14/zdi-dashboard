# ZDI-20-630: Advantech WebAccess/SCADA DrawSrv IOCTL 0x00002722 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-630
- **ZDI-CAN:** ZDI-CAN-9896
- **Date:** 2020-05-08
- **CVE:** CVE-2020-12018
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-630/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of IOCTL 0x00002722 in DrawSrv.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2020-02-12 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
