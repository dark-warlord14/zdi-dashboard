# ZDI-22-932: Advantech iView findCfgDeviceListDetailsExport filename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-932
- **ZDI-CAN:** ZDI-CAN-16702
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2139
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-932/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. When parsing the filename element of the findCfgDeviceListDetailsExport action, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-09 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
