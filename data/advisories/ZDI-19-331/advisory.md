# ZDI-19-331: Advantech WebAccess Node UninstallWA Improper Access Control Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-331
- **ZDI-CAN:** ZDI-CAN-7908
- **Date:** 2019-04-02
- **CVE:** CVE-2019-6554
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-331/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within UninstallWA.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. An attacker can leverage this vulnerability to uninstall the application and create a denial-of-service condition on the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-092-01

## Disclosure Timeline

- 2019-01-22 - Vulnerability reported to vendor
- 2019-04-02 - Coordinated public release of advisory
