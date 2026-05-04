# ZDI-15-238: (0Day) Visual Mining NetCharts Server Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-238
- **ZDI-CAN:** ZDI-CAN-2596
- **Date:** 2015-05-22
- **CVE:** CVE-2015-4032
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Visual Mining
- **Affected Products:** NetCharts Server
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-238/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Visual Mining NetCharts Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Developer tools. An attacker can use the projectContents.jsp page to rename an arbitrary file, allowing for an uploaded file to be executed. This allows an attacker to execute arbitrary code as SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 11/19/2014 - ZDI disclosed report to Visual Mining Technical Support Team. 03/13/2015 - ZDI requested a status update. 04/22/2015 - ZDI requested a status update. 05/18/2015 - ZDI requested a status update. ZDI has recieved no replies from the vendor to our requests for updates. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-11-19 - Vulnerability reported to vendor
- 2015-05-22 - Coordinated public release of advisory
