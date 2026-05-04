# ZDI-18-024: Advantech WebAccess webvrpcs Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-024
- **ZDI-CAN:** ZDI-CAN-4992
- **Date:** 2018-09-13
- **CVE:** CVE-2017-16720
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this functionality to execute code under the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-004-02

## Disclosure Timeline

- 2017-09-06 - Vulnerability reported to vendor
- 2018-09-13 - Coordinated public release of advisory
- 2018-09-13 - Advisory Updated
