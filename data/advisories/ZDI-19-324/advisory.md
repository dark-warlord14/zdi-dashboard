# ZDI-19-324: Advantech WebAccess Client bwrunmie Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-324
- **ZDI-CAN:** ZDI-CAN-7926
- **Date:** 2019-04-02
- **CVE:** CVE-2019-6552
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-324/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Client. Authentication is not required to exploit this vulnerability. The specific flaw exists within bwrunmie.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-092-01

## Disclosure Timeline

- 2019-01-24 - Vulnerability reported to vendor
- 2019-04-02 - Coordinated public release of advisory
