# ZDI-17-288: Oracle Fusion Middleware MapViewer FileUploaderServlet fileName Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-288
- **ZDI-CAN:** ZDI-CAN-3988
- **Date:** 2017-04-19
- **CVE:** CVE-2017-3230
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Fusion Middleware MapViewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Fusion Middleware MapViewer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileUploaderServlet servlet. When parsing the fileName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuapr2017-3236618.html

## Disclosure Timeline

- 2016-09-06 - Vulnerability reported to vendor
- 2017-04-19 - Coordinated public release of advisory
