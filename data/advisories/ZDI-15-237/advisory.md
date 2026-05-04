# ZDI-15-237: (0Day) Visual Mining NetCharts Server Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-237
- **ZDI-CAN:** ZDI-CAN-2492
- **Date:** 2015-05-22
- **CVE:** CVE-2015-4031
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Visual Mining
- **Affected Products:** NetCharts Server
- **Credit:** bart
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-237/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Visual Mining NetChart. Authentication is not required to exploit this vulnerability. The specific flaw exists within the development installation. The saveFile.jsp page does not properly check for directory traversal, allowing an attacker to overwrite any file on the system. An attacker could leverage this to execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 9/11/2014 - ZDI disclosed report to Visual Mining Technical Support Team. 9/12/2014 - Visual Mining Technical Support Team notified that Visual Mining is now a division of Tervela, Inc. They asked ZDI to re-disclose with a new encryption key. 9/15/2014 - ZDI re-disclosed report to Visual Mining Technical Support Team using the new key. 2/23/2015 - ZDI requested a status update. 3/13/2015 - ZDI requested a status update. 4/22/2015 - ZDI requested a status update. ZDI has recieved no replies from the vendor to our requests for updates. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-09-11 - Vulnerability reported to vendor
- 2015-05-22 - Coordinated public release of advisory
