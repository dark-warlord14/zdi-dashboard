# ZDI-10-003: Novell ZENworks Asset Management docfiledownload Remote SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-003
- **ZDI-CAN:** ZDI-CAN-457
- **Date:** 2010-01-12
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Asset Management. Authentication is not required to exploit this vulnerability. The specific flaw exists due to insufficient sanity checks on the documentID parameter to the docfiledownload component. A carefully crafted parameter can result in direct SQL access to the underlying SQL Server database which can be further leveraged by an attacker to potentially execute arbitrary code.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7005128&sliceId=1

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2010-01-12 - Coordinated public release of advisory
