# ZDI-11-113: Zend Server Java Bridge Design Flaw Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-113
- **ZDI-CAN:** ZDI-CAN-928
- **Date:** 2011-03-28
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Zend
- **Affected Products:** Zend Server
- **Credit:** Luca Carettoni
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Zend Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Zend Java Bridge v3.1 component of the Zend Server framework. The javamw.jar service accepts TCP requests on port 10001 by default. With nothing more than the knowledge of the proprietary communication protocol used by the Zend Server Java Bridge, it is possible to send arbitrary Java code to javamw.jar service and remotely execute these commands under the context of the user running the web server process.

## Additional Details

Zend Server Java Bridge Hotfix http://www.zend.com/en/products/server/downloads Mention and notification can also be found here: http://www.zend.com/en/products/server/updates

## Disclosure Timeline

- 2010-09-30 - Vulnerability reported to vendor
- 2011-03-28 - Coordinated public release of advisory
