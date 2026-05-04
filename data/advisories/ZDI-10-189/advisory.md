# ZDI-10-189: Novell eDirectory Server Malformed Index Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-189
- **ZDI-CAN:** ZDI-CAN-477
- **Date:** 2010-10-01
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-189/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Novell eDirectory. Authentication is not required in order to trigger this vulnerability. The flaw exists within Novell's eDirectory Server's NCP implementation which binds, by default, to TCP port 524. While handling a malformed request, the application explicitly trusts a field when translating it to an index into a table of counters. If this index is too large, the application will set a value outside the array and the ndsd process will become unresponsive resulting in an inability to authenticate to that server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7006389&sliceId=2

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2010-10-01 - Coordinated public release of advisory
