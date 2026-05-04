# ZDI-16-038: Oracle Application Testing Suite ReportImage tempfilename Parameter Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-038
- **ZDI-CAN:** ZDI-CAN-3323
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0489
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Application Testing Suite. Authentication is required but can be bypassed. The specific vulnerability is exposed by the ActionServlet servlet. In the ReportImage action, the tempfilename parameter is vulnerable to directory traversal. An attacker could leverage this to execute arbitrary code under the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
