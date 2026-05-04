# ZDI-12-088: HP DataDirect OpenAccess GIOP Opcode 0x0E Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-088
- **ZDI-CAN:** ZDI-CAN-1213
- **Date:** 2012-06-06
- **CVE:** CVE-2011-4163
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard, DataDirect
- **Affected Products:** Database Archiving, SequeLink
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP DataDirect SequeLink. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the application parses a packet that is received. When parsing a field in this packet, the application will use a signed length to copy data into a statically sized buffer located on the stack. This can lead to a buffer overflow on the stack and allow for code execution under the context of the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302 DataDirect has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
