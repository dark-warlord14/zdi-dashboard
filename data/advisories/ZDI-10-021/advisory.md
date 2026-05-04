# ZDI-10-021: Novell NetStorage xsrvd Long Pathname Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-021
- **ZDI-CAN:** ZDI-CAN-607
- **Date:** 2010-02-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** NetStorage
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell NetStorage. Authentication is not required to exploit this vulnerability. The specific flaws exists within the xsrvd process during the wide character conversion of requested file paths. In conjunction with a long username value the file path conversion will result in a heap overflow corrupting a chunk that will be immediately freed. This can be leveraged by remote attackers to compromise the NetStorage server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7005282

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-02-23 - Coordinated public release of advisory
