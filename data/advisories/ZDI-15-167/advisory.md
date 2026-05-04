# ZDI-15-167: ManageEngine Desktop Central MSP IOSCheckInServlet UDID Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-167
- **ZDI-CAN:** ZDI-CAN-2471
- **Date:** 2015-05-06
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** Destkop Central MSP
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-167/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine Desktop Central MSP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IOSCheckInServlet servlet. The issue lies in the failure to sanitize JSON data before processing it. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Upgrade to version 9 build 90066 or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-19 - Vulnerability reported to vendor
- 2015-05-06 - Coordinated public release of advisory
