# ZDI-20-617: Advantech WebAccess/SCADA BwWebSvc IOCTL 0x00013c7b Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-617
- **ZDI-CAN:** ZDI-CAN-9890
- **Date:** 2020-05-08
- **CVE:** CVE-2020-10638
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-617/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of IOCTL 0x00013c7b in BwWebSvc.dll. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2020-02-05 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
