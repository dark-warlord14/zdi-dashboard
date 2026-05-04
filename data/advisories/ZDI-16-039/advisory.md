# ZDI-16-039: Oracle Application Testing Suite filename Header Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-039
- **ZDI-CAN:** ZDI-CAN-3306
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0490
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Application Testing Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UploadServlet servlet. By providing a filename header containing a directory traversal, an attacker is able to write a file to an arbitrary location on the system. An attacker can leverage this to execute arbitrary code under the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-06 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
