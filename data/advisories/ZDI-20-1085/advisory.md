# ZDI-20-1085: Advantech iView DeviceTreeTable exportInventoryTable Directory Traversal File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1085
- **ZDI-CAN:** ZDI-CAN-10988
- **Date:** 2020-08-27
- **CVE:** CVE-2020-16245
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** KPC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1085/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the exportInventoryTable method of the DeviceTreeTable class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-238-01

## Disclosure Timeline

- 2020-07-07 - Vulnerability reported to vendor
- 2020-08-27 - Coordinated public release of advisory
