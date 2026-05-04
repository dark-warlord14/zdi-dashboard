# ZDI-11-060: Novell eDirectory Malformed NCP Request Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-060
- **ZDI-CAN:** ZDI-CAN-445
- **Date:** 2011-02-07
- **CVE:** CVE-2010-4327
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-060/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Novell eDirectory. Authentication is not required in order to trigger this vulnerability. The flaw exists within Novell's eDirectory Server's NCP implementation. Novell's eDirectory Server binds to port 524 for processing NCP requests. When the application processes a malformed FileSetLock request, the service will become unresponsive resulting in an inability to authenticate to that server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7007781&sliceId=2

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
