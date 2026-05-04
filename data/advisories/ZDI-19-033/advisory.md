# ZDI-19-033: Oracle Java jnlp Protocol Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-033
- **ZDI-CAN:** ZDI-CAN-7151
- **Date:** 2019-01-16
- **CVE:** CVE-2019-2449
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-033/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of URIs with the jnlp: protocol. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-08-17 - Vulnerability reported to vendor
- 2019-01-16 - Coordinated public release of advisory
