# ZDI-12-099: DataDirect OpenAccess oaagent.exe GIOP Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-099
- **ZDI-CAN:** ZDI-CAN-1263
- **Date:** 2012-06-21
- **CVE:** CVE-2011-4165
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard, DataDirect
- **Affected Products:** Database Archiving, SequeLink
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of DataDirect SequeLink. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the application parses a packet that is received. When parsing a field in this packet, the application will use a signed length to copy data into a statically sized buffer located on the heap. This can lead to a heap-based buffer overflow and allows for code execution under the context of the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302 DataDirect has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
