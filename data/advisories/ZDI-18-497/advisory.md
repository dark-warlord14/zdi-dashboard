# ZDI-18-497: Advantech WebAccess Node bwmakdir Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-497
- **ZDI-CAN:** ZDI-CAN-5662
- **Date:** 2018-05-18
- **CVE:** CVE-2018-7499
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-497/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within bwmakdir.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this functionality to execute code under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-02-09 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
