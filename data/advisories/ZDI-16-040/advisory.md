# ZDI-16-040: Oracle Application Testing Suite DownloadServlet exportFileName Parameter Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-040
- **ZDI-CAN:** ZDI-CAN-3308
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0486
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-040/
## Vulnerability Details

This vulnerability allows remote attackers to exfiltrate arbitrary files on vulnerable installations of Oracle Application Testing Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DownloadServlet servlet. By providing an exportFileName parameter containing a directory traversal where the downloadType is specified as OTMExportFile, an attacker can exfiltrate arbitrary files from the system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-01 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
