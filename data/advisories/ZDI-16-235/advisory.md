# ZDI-16-235: Adobe Creative Cloud Node.js Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-235
- **ZDI-CAN:** ZDI-CAN-3543
- **Date:** 2016-04-12
- **CVE:** CVE-2016-1034
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Creative Cloud
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-235/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Creative Cloud. Authentication is not required to exploit this vulnerability. The application exposes a services that listens on a random TCP port. The lack of authentication in the exposed service allows remote users to execute various methods from the API exposed by this service. An attacker can leverage this to execute code under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/creative-cloud/apsb16-11.html

## Disclosure Timeline

- 2016-02-16 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
