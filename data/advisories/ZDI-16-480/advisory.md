# ZDI-16-480: Samsung Security Manager ActiveMQ Broker Service DELETE Method Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-480
- **ZDI-CAN:** ZDI-CAN-3548
- **Date:** 2016-08-18
- **CVE:** N/A
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Security Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-480/
## Vulnerability Details

This vulnerability allows remote attackers to delete files of their choosing from systems running vulnerable installations of Samsung Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ActiveMQ Broker service that is installed as part of this product. By issuing an HTTP DELETE request, an attacker can delete files that reside on the server. If desired, the attacker could delete critical files, rendering the server unusable.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: http://security.hanwhatechwin.com/product/product_view.asp?idx=6779#FL080000

## Disclosure Timeline

- 2016-02-15 - Vulnerability reported to vendor
- 2016-08-18 - Coordinated public release of advisory
