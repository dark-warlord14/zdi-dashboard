# ZDI-12-146: Novell eDirectory RelativeToFullDN Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-146
- **ZDI-CAN:** ZDI-CAN-1409
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-146/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the service handles a specially formatted LDAP request. When handling a particular set of commands, the server will copy a string described in the packet into a statically sized buffer without validating it's length. This leads to a stack-based overflow and as such can be exploited to achieve code execution under the context of the application.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7009947

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
