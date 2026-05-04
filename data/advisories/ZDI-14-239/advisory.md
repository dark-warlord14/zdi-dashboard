# ZDI-14-239: Apache HTTP Server mod_proxy Denial Of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-239
- **ZDI-CAN:** ZDI-CAN-2241
- **Date:** 2014-07-18
- **CVE:** CVE-2014-0117
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Apache
- **Affected Products:** HTTPD Server 2.x
- **Credit:** AKAT-1 22733db72ab3ed94b5f8a1ffcde850251fe6f466 Marek Kroemeke
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-239/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service condition on vulnerable installations of Apache HTTP Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mod_proxy module. The issue lies in the processing of HTTP headers when an invalid request is made. An attacker can leverage this flaw to crash a remote instance of Apache HTTP server.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://httpd.apache.org/security/vulnerabilities_24.html

## Disclosure Timeline

- 2014-04-07 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
