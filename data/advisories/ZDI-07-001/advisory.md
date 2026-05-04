# ZDI-07-001: QUALCOMM Eudora WorldMail Remote Management Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-001
- **ZDI-CAN:** ZDI-CAN-073
- **Date:** 2007-01-05
- **CVE:** CVE-2006-6336
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** QUALCOMM
- **Affected Products:** Eudora
- **Credit:** Leon Juranic, INFIGO IS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-001/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Eudora WorldMail. Authentication is not required to exploit this vulnerability. The specific flaw exists during the parsing of successive delimiters within the Mail Management Server, MAILMA.exe, listening on TCP port 106. Processing a maliciously crafted request can result in an exploitable heap corruption.

## Additional Details

QUALCOMM will not be addressing this issue with a software patch and instead recommends that administrators block access to the affected port from untrusted sources at the network level.

## Disclosure Timeline

- 2006-09-15 - Vulnerability reported to vendor
- 2007-01-05 - Coordinated public release of advisory
