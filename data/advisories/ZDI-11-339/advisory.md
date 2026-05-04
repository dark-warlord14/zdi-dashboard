# ZDI-11-339: Iron Mountain Connected Backup Agent Unauthenticated Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-339
- **ZDI-CAN:** ZDI-CAN-1023
- **Date:** 2011-12-01
- **CVE:** CVE-2011-2397
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Iron Mountain
- **Affected Products:** Connected Backup 8.4
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-339/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Iron Mountain Connected Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Agent service that listens by default on TCP port 16388. When dealing with a request containing the opcode 13, the java process instantiates an instance of a class called LaunchCompoundFileAnalyzer. This class passes user-controlled data directly to System.getRunTime.exec. This can be abused to execute remote code on the agent process under the context of the user running the software.

## Additional Details

Versions affected 8.2.2 - 8.5.1 Fixed versions: 8.2.2.3, 8.4.0.13, 8.4.1.1, 8.5.1.1 and later (including all 8.6.x) Customers were notified and updates released 5/9/2011. Updated versions are available through normal support channels ( http://customers.autonomy.com , http://digitalresourcecenter.ironmountain.com )

## Disclosure Timeline

- 2011-04-25 - Vulnerability reported to vendor
- 2011-12-01 - Coordinated public release of advisory
