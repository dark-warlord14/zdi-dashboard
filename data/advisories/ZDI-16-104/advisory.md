# ZDI-16-104: Advantech WebAccess datacore Service datacore.exe ExtDataSize Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-104
- **ZDI-CAN:** ZDI-CAN-3197
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0859
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x791E IOCTL in the Kernel subsystem. An integer overflow for alloc size vulnerability exists. An attacker can use this vulnerability to execute arbitrary code in the context of an administrator of the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
