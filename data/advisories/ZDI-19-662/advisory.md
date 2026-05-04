# ZDI-19-662: Oracle Database ODBC Driver Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-662
- **ZDI-CAN:** ZDI-CAN-7226
- **Date:** 2019-07-22
- **CVE:** CVE-2019-2799
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Database
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-662/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Database. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ODBC driver. When parsing certain attributes, the process does not properly validate user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html

## Disclosure Timeline

- 2019-01-17 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
