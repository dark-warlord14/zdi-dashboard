# ZDI-15-220: ManageEngine EventLog Analyzer UploadHandlerServlet File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-220
- **ZDI-CAN:** ZDI-CAN-2425
- **Date:** 2015-05-13
- **CVE:** CVE-2014-6037
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** EventLog Analyzer
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-220/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine EventLog Analyzer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UploadHandlerServlet servlet. The issue lies in the failure to sanitize the filenames uploaded to the servlet. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Upgrade to version 10.0 build 10001 or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-05-13 - Coordinated public release of advisory
