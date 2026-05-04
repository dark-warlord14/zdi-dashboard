# ZDI-11-273: EMC Autostart Domain Name Logging Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-273
- **ZDI-CAN:** ZDI-CAN-1078
- **Date:** 2011-08-23
- **CVE:** CVE-2011-2735
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-273/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC AutoStart High Availability. Authentication is not required to exploit this vulnerability. The specific flaw exists within the packet error handling of the application. When building an error message to log an error, the application will use a user-supplied string from the packet as an argument to a function containing a format string. The result of this function is written to a statically sized buffer located on the stack. This will lead to code execution under the context of the service.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/519371

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-08-23 - Coordinated public release of advisory
