# ZDI-12-089: HP DataDirect OpenAccess GIOP Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-089
- **ZDI-CAN:** ZDI-CAN-1214
- **Date:** 2012-06-06
- **CVE:** CVE-2011-4164
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard, DataDirect
- **Affected Products:** Database Archiving, SequeLink
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable applications using DataDirect's SequeLink. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the application processes GIOP packets. When processing a specific GIOP packet, the application will trust a size field in the packet. The application will use this size in a copy operation into a statically sized buffer which can cause a buffer overflow. This can lead to code execution under the context of the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302 DataDirect has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128302

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
