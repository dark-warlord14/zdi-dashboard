# ZDI-12-140: McAfee SmartFilter Administration Server SFAdminSrv.exe JBoss RMI Remote Code Execution Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-12-140
- **ZDI-CAN:** ZDI-CAN-1406
- **Date:** 2012-08-17
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** McAfee
- **Affected Products:** Smart Filter
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of McAfee SmartFilter Administration Server. Authentication is not required to exploit this vulnerability. The flaw exists within the Remote Method Invocation (RMI) component which is exposed by SFAdminSrv.exe process. This process exposes various RMI services to TCP ports 4444 (JBoss RMI HTTPInvoker), 1098 (rmiactivation), 1099 (rmiregistry). Requests to these services are not authenticated and can be used to instantiate arbitrary classes or to upload and execute arbitrary archives. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10029

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
