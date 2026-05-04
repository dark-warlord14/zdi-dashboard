# ZDI-10-073: Sun Microsystems Directory Server DSML-over-HTTP Username Search Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-073
- **ZDI-CAN:** ZDI-CAN-594
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0897
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Directory Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-073/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Sun Microsystems Directory Service Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within Sun Directory Server's DSML-over-HTTP implementation and can be triggered via an HTTP POST request to the webserver that the application has bound to. When the service processes a search request with a malformed username, the application will dereference a null pointer causing any future queries made against the webserver to fail. This will lead to a denial of service against the affected service.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2010.html

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
