# ZDI-12-022: Total Defense Suite UNC Management Console ExportReport SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-022
- **ZDI-CAN:** ZDI-CAN-1121
- **Date:** 2012-02-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Total Defense
- **Affected Products:** CA Total Defense
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Total Defense Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ExportReport stored procedure, accessed via the management.asmx console. The Management Web Service listens for SOAP 1.2 requests on port 34444 for HTTP and 34443 for HTTPS. Due to a flaw in the implementation of the ExportReport stored procedure, it is possible for a remote, unauthenticated user to inject arbitrary SQL commands in the SOAP request--which could ultimately lead to arbitrary code execution under the context of the SYSTEM user by invoking an exec function.

## Additional Details

We are pleased to confirm that all three vulns that were reported by Tipping Point were proactively closed as part of the Total Defense R12 SE3 (Build 831) release cycle. This SE3 release is publicly shipping from our download links since December 5th, 2011. Physical media (DVD) is currently in production for those clients seeking that option as opposed to a download and we will be shipping those DVDs in early January 2012 based on the production schedule.

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
