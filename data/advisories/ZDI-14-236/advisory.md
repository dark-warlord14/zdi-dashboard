# ZDI-14-236: Apache httpd mod_status Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-236
- **ZDI-CAN:** ZDI-CAN-2340
- **Date:** 2014-07-16
- **CVE:** CVE-2014-0226
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apache
- **Affected Products:** HTTPD Server 2.x
- **Credit:** AKAT-1 22733db72ab3ed94b5f8a1ffcde850251fe6f466 Marek Kroemeke
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-236/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache HTTPD server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the updating of mod_status. A race condition in mod_status allows an attacker to disclose information or corrupt memory with several requests to endpoints with handler server-status and other endpoints. By abusing this flaw, an attacker can possibly disclose credentials or leverage this situation to achieve remote code execution.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://mail-archives.apache.org/mod_mbox/httpd-cvs/201407.mbox/%3C20140714195504.EF60D23889E2@eris.apache.org%3E

## Disclosure Timeline

- 2014-05-30 - Vulnerability reported to vendor
- 2014-07-16 - Coordinated public release of advisory
