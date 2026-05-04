# ZDI-10-075: Sun Microsystems Directory Server Enterprise DSML UTF-8 Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-075
- **ZDI-CAN:** ZDI-CAN-609
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0897
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Directory Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-075/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Sun Microsystems Directory Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within Sun Directory Server's DSML-over-HTTP implementation and can be triggered via an HTTP POST request to the webserver that the application has bound to. When the service processes an XML request containing specific UTF-8 characters, an underlying library will raise an exception that is uncaught by the application. Due to the exception being uncaught, the application will then terminate which will cause future requests made against the service to fail. This will lead to a denial of service against the affected application.

## Additional Details

http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2010.html

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
