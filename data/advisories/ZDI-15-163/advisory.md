# ZDI-15-163: ManageEngine Desktop Central MSP MDMLogUploaderServlet filename File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-163
- **ZDI-CAN:** ZDI-CAN-2442
- **Date:** 2015-04-29
- **CVE:** CVE-2014-5006
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** Destkop Central MSP
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-163/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine Desktop Central MSP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MDMLogUploaderServlet servlet. The issue lies in the failure to sanitize the filenames uploaded to the servlet. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Upgrade to version 9 Build 90055, or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
