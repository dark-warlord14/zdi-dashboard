# ZDI-10-187: IBM TSM FastBack Server _DAS_ReadBlockReply Remote Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-187
- **ZDI-CAN:** ZDI-CAN-664
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-187/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of IBM Tivoli FastBack Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe process which listens by default on TCP port 11406. The problematic code resides within a function responsible for reading a block of network packet data. A parameter to this function is initialized to 0 and under certain conditions this value will be accessed before properly initialized. This causes a NULL pointer to be dereferenced and subsequent application crash due to a lack of exception handling. Successful exploitation leads to immediate termination of the fastback server.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 3

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory
