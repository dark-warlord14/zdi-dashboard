# ZDI-19-845: Advantech WebAccess Node bwgetval Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-845
- **ZDI-CAN:** ZDI-CAN-9270
- **Date:** 2019-09-17
- **CVE:** CVE-2019-13552
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-845/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within bwgetval.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-260-01

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2019-09-17 - Coordinated public release of advisory
