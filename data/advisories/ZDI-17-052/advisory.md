# ZDI-17-052: Brocade Network Advisor CliMonitorReportServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-052
- **ZDI-CAN:** ZDI-CAN-4026
- **Date:** 2017-01-20
- **CVE:** CVE-2016-8207
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Brocade
- **Affected Products:** Network Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-052/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Brocade Network Advisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CliMonitorReportsServlet servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Brocade has issued an update to correct this vulnerability. More details can be found at: https://www.brocade.com/content/dam/common/documents/content-types/security-bulletin/brocade-security-advisory-2016-180.htm

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
