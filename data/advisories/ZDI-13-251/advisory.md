# ZDI-13-251: MySQL yaSSL Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-251
- **ZDI-CAN:** ZDI-CAN-1578
- **Date:** 2013-11-24
- **CVE:** CVE-2013-1492
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** MySQL
- **Affected Products:** MySQL
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of MySQL with yaSSL. Authentication is not required to exploit this vulnerability. The specific flaw exists within the yaSSL library that is optionally used by MySQL for SSL communication. There exists an off-by-one overflow that is repeatedly performed during the SSL handshake. This can result in memory corruption that can lead to remote code execution under the context of the current process.

## Additional Details

MySQL has issued an update to correct this vulnerability. More details can be found at: https://blogs.oracle.com/sunsecurity/entry/cve_2013_1492_buffer_overflow

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
