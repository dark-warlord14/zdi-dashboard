# ZDI-14-056: Avaya IP Office one-X Portal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-056
- **ZDI-CAN:** ZDI-CAN-1688
- **Date:** 2014-04-03
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Avaya
- **Affected Products:** IP Office
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Avaya IP Office one-X Portal. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UserConfigurationService and UploadFromLocalDriveServlet servlets. The UserConfigurationService servlet does not properly validate user-supplied data allowing for the super user account to be reset. The UploadFromLocalDriveServlet servlet also fails to validate user-supplied data allowing for arbitrary file writes with SYSTEM level privileges. An attacker can leverage these vulnerabilities to execute code with SYSTEM level privileges.

## Additional Details

Avaya has issued an update to correct this vulnerability. More details can be found at: https://downloads.avaya.com/css/P8/documents/100178987

## Disclosure Timeline

- 2013-04-14 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
