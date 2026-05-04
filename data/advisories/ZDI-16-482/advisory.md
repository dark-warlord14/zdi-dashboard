# ZDI-16-482: Samsung Security Manager ActiveMQ Broker Service MOVE Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-482
- **ZDI-CAN:** ZDI-CAN-3549
- **Date:** 2016-08-18
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Security Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-482/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ActiveMQ Broker service that is installed as part of this product. By issuing an HTTP PUT request and an HTTP MOVE request, an attacker can create an arbitrary file on the server with attacker controlled data. An attacker can further leverage this vulnerability to execute code on the server as SYSTEM.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: http://security.hanwhatechwin.com/product/product_view.asp?idx=6779#FL080000

## Disclosure Timeline

- 2016-02-15 - Vulnerability reported to vendor
- 2016-08-18 - Coordinated public release of advisory
