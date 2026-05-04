# ZDI-20-1088: Advantech iView NetworkServlet backupDatabase Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1088
- **ZDI-CAN:** ZDI-CAN-10991
- **Date:** 2020-08-27
- **CVE:** CVE-2020-16245
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** KPC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1088/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the backupDatabase method of the NetworkServlet class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to overwrite arbitrary files and also to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-238-01

## Disclosure Timeline

- 2020-07-07 - Vulnerability reported to vendor
- 2020-08-27 - Coordinated public release of advisory
