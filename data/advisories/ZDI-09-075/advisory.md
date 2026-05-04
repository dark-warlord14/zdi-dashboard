# ZDI-09-075: Novell eDirectory LDAP Null Base DN Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-075
- **ZDI-CAN:** ZDI-CAN-513
- **Date:** 2009-11-02
- **CVE:** CVE-2009-3862
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-075/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Novell eDirectory. Authentication is not required in order to exploit this vulnerability. The specific flaw exists within Novell's eDirectory Server's LDAP implementation. Novell eDirectory's NDSD process binds to port 389/TCP for handling LDAP requests. When the service processes a search request with an undefined BaseDN, it will become unresponsive resulting in an inability to query or authenticate to that server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7004721

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2009-11-02 - Coordinated public release of advisory
