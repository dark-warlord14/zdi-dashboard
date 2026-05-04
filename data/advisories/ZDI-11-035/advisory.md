# ZDI-11-035: IBM DB2 db2dasrrm validateUser Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-035
- **ZDI-CAN:** ZDI-CAN-775
- **Date:** 2011-01-31
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** IBM
- **Affected Products:** DB2 Universal Database
- **Credit:** Intevydis http://intevydis.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM DB2. Authentication is not required to exploit this vulnerability. The specific flaw exists within the db2dasrrm process responsible for handling queries to the com.ibm.db2.das.core.DasSysCmd function. While processing a request, the username supplied is copied into a fixed-length stack buffer. By providing a large enough string the copy operation can overflow leading to remote code execution.

## Additional Details

https://www-304.ibm.com/support/docview.wss?uid=swg21426108 v9.1 fp10 IC69986 https://www-304.ibm.com/support/docview.wss?uid=swg1IC69986 v9.5 fp6 IC70538 https://www-304.ibm.com/support/docview.wss?uid=swg1IC70538 v9.7 fp3 IC70539 https://www-304.ibm.com/support/docview.wss?uid=swg1IC70539

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2011-01-31 - Coordinated public release of advisory
