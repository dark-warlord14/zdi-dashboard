# ZDI-11-032: Symantec Intel Alert Originator Service iao.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-032
- **ZDI-CAN:** ZDI-CAN-580
- **Date:** 2011-01-27
- **CVE:** CVE-2010-0111
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Alert Management System
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of multiple Symantec products. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Intel Alert Originator (iao.exe) service. While processing messages sent from the msgsys.exe process a size check can be bypassed and a subsequent stack-based buffer overflow can be triggered. This can be leveraged by remote attackers to execute arbitrary code under the context of the Alert service.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110126_00

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2011-01-27 - Coordinated public release of advisory
