# ZDI-20-1091: Advantech iView NetworkServlet findUpdateDeviceListExport Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1091
- **ZDI-CAN:** ZDI-CAN-10994
- **Date:** 2020-08-27
- **CVE:** CVE-2020-16245
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** KPC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the findUpdateDeviceListExport method of the NetworkServlet class. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-238-01

## Disclosure Timeline

- 2020-07-07 - Vulnerability reported to vendor
- 2020-08-27 - Coordinated public release of advisory
