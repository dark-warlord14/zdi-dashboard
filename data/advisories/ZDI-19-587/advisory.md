# ZDI-19-587: Advantech WebAccess Node webvrpcs viewsrv Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-587
- **ZDI-CAN:** ZDI-CAN-7952
- **Date:** 2019-07-02
- **CVE:** CVE-2019-10987
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson(@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-587/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2723 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-178-05

## Disclosure Timeline

- 2019-02-22 - Vulnerability reported to vendor
- 2019-07-02 - Coordinated public release of advisory
