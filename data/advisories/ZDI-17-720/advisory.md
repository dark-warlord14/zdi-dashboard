# ZDI-17-720: Hewlett Packard Enterprise Application Performance Management System Health SHExportToExcel Servlet Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-720
- **ZDI-CAN:** ZDI-CAN-4457
- **Date:** 2017-09-07
- **CVE:** CVE-2017-13984
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Application Performance Management System Health
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-720/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Hewlett Packard Enterprise Application Performance Management System Health. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SHExportToExcel servlet, which listens on TCP port 18080 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any file accessible to the SYSTEM account.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.hpe.com/km/KM02942065

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-09-07 - Coordinated public release of advisory
