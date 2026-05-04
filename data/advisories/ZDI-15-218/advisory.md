# ZDI-15-218: ManageEngine Desktop Central MSP DSStatusUpdateServlet DomainName File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-218
- **ZDI-CAN:** ZDI-CAN-2444
- **Date:** 2015-05-13
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** Destkop Central MSP
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-218/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine Desktop Central MSP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DSStatusUpdateServlet servlet. The issue lies in the failure to sanitize the filenames uploaded to the servlet. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Upgrade to version 9 build 90142 or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-05-13 - Coordinated public release of advisory
