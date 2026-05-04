# ZDI-14-106: Oracle Event Processing FileUploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-106
- **ZDI-CAN:** ZDI-CAN-2048
- **Date:** 2014-04-21
- **CVE:** CVE-2014-2424
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Event Processing
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Event Processing. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileUploadServlet class. The class contains a method that does not properly sanitize input allowing for directory traversal. An attacker can leverage this vulnerability to write files under the context of the user and achieve remote code execution.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2014-1972952.html

## Disclosure Timeline

- 2013-12-09 - Vulnerability reported to vendor
- 2014-04-21 - Coordinated public release of advisory
