# ZDI-19-582: Apache Tomcat reserveWindowSize Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-582
- **ZDI-CAN:** ZDI-CAN-8630
- **Date:** 2019-06-21
- **CVE:** CVE-2019-10072
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Apache
- **Affected Products:** Tomcat
- **Credit:** John Simpson of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-582/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on vulnerable installations of Apache Tomcat. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP2 requests. A crafted HTTP2 request can create a deadlock on a worker thread. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://tomcat.apache.org/security-9.html

## Disclosure Timeline

- 2019-04-26 - Vulnerability reported to vendor
- 2019-06-21 - Coordinated public release of advisory
