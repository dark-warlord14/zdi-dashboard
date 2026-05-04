# ZDI-12-151: Oracle Outside In Excel File TxO Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-151
- **ZDI-CAN:** ZDI-CAN-1482
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** gwlabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of products utilizing Oracle's Outside In Technology. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the library's parsing of Excel files. When handling the TxO record, the vseshr.dll module can be made to wrap an integer value when parsing a specific field. This can lead to an improper memory allocation that can be leveraged to corrupt the heap leading to arbitrary code execution under the context of the user running the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2012-366314.html

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
