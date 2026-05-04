# ZDI-18-1369: Apache2 mod_http2 header Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1369
- **ZDI-CAN:** ZDI-CAN-7168
- **Date:** 2018-12-10
- **CVE:** CVE-2018-11763
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Apache
- **Affected Products:** HTTPD Server 2.x
- **Credit:** David Fiser
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1369/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of Apache HTTPD server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP2 headers. A crafted HTTP2 request can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11763

## Disclosure Timeline

- 2018-08-22 - Vulnerability reported to vendor
- 2018-12-10 - Coordinated public release of advisory
