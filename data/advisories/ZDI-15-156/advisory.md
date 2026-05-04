# ZDI-15-156: Samsung Security Manager ActiveMQ Broker Service PUT Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-156
- **ZDI-CAN:** ZDI-CAN-2337
- **Date:** 2015-04-29
- **CVE:** CVE-2015-3435
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Security Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-156/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Security Manager. Authentication is not required to exploit this vulnerability. Successful exploitation allows an attacker to gain complete control of the system on which the product is installed. The specific flaw exists within the ActiveMQ Broker service that is installed as part of this product. By issuing an HTTP PUT request, an attacker can create an arbitrary file on the server with attacker controlled data. An attacker can further leverage this vulnerability to execute code on the server as the SYSTEM user, thereby gaining complete control of the server.

## Additional Details

Samsung has issued the following update to resolve this issue: SSM 1.31 or higher ( http://www.samsungsecurity.com/swdown/download.asp )

## Disclosure Timeline

- 2014-07-28 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
