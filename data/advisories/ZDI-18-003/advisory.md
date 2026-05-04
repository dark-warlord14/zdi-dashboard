# ZDI-18-003: Hewlett Packard Enterprise Moonshot Provisioning Manager Appliance server_response Directory Traversal Denial Of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-003
- **ZDI-CAN:** ZDI-CAN-4945
- **Date:** 2018-01-03
- **CVE:** CVE-2017-8977
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Moonshot Provisioning Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-003/
## Vulnerability Details

This vulnerability allows remote attackers to overwrite arbitrary files on vulnerable installations of Hewlett Packard Enterprise Moonshot Provisioning Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the server_response.py file. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to overwrite any file accessible to the root user and create a denial-of-service condition.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03803en_us

## Disclosure Timeline

- 2017-07-05 - Vulnerability reported to vendor
- 2018-01-03 - Coordinated public release of advisory
