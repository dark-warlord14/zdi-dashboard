# ZDI-17-721: Hewlett Packard Enterprise Application Performance Management System Health Email Servlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-721
- **ZDI-CAN:** ZDI-CAN-4456
- **Date:** 2017-09-07
- **CVE:** CVE-2017-13985
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Application Performance Management System Health
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-721/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Application Performance Management System Health. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Email servlet, which listens on TCP port 18080 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.hpe.com/km/KM02942065

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-09-07 - Coordinated public release of advisory
