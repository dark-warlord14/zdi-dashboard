# ZDI-12-202: Oracle Outside In WordPerfect File Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-202
- **ZDI-CAN:** ZDI-CAN-1480
- **Date:** 2012-12-21
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-202/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable products utilizing the Oracle Outside In technology. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WordPerfect files. When parsing font records the code within vswp5.dll does not validate the datasize value prior to performing arithmetic on it. The result is used to make a heap allocation that can be undersized which can be leveraged to corrupt memory leading to arbitrary code execution under the context of the user running the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
