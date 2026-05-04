# ZDI-18-483: Advantech WebAccess webvrpcs Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-483
- **ZDI-CAN:** ZDI-CAN-5627
- **Date:** 2018-05-18
- **CVE:** CVE-2018-10589
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-483/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this functionality to execute code under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-02-09 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-09-13 - Advisory Updated
