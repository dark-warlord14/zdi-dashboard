# ZDI-20-626: Advantech WebAccess/SCADA ViewSrv IOCTL 0x0000277d Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-626
- **ZDI-CAN:** ZDI-CAN-9907
- **Date:** 2020-05-08
- **CVE:** CVE-2020-12026
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-626/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess/SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of IOCTL 0x0000277d in ViewSrv.dll. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
