# ZDI-16-047: Oracle Application Testing Suite UploadFileAction Servlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-047
- **ZDI-CAN:** ZDI-CAN-3302
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0491
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Application Testing Suite. Authentication is required but can be bypassed. The specific vulnerability is in the UploadFileAction servlet. By providing a fileType parameter of "*", an attacker is able to upload a file to an arbitrary location on the system. An attacker could leverage this to execute arbitrary code under the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-06 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
