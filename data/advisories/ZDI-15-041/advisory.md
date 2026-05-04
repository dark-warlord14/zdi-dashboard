# ZDI-15-041: Samsung Security Manager ActiveMQ Broker Service DELETE Method Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-041
- **ZDI-CAN:** ZDI-CAN-2339
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1499
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Security Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-041/
## Vulnerability Details

This vulnerability allows remote attackers to delete files of their choosing from systems running vulnerable installations of Samsung Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ActiveMQ Broker service that is installed as part of this product. By issuing an HTTP DELETE request, an attacker can delete files that reside on the server. The attacker may choose to delete critical files, rendering the server unusable.

## Additional Details

Samsung has issued the following update to resolve this issue: SSM 1.31 or higher ( http://www.samsungsecurity.com/swdown/download.asp )

## Disclosure Timeline

- 2014-07-28 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
