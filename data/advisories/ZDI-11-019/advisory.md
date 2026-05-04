# ZDI-11-019: Oracle GoldenGate Veridata Server XML SOAP Request Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-019
- **ZDI-CAN:** ZDI-CAN-800
- **Date:** 2011-01-18
- **CVE:** CVE-2010-4416
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** GoldenGate Veridata Server
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle GoldenGate Veridata. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way the application parses an XML soap request used for authorization to the management site. While copying string data from a tag into a buffer, the application will terminate the copy only when the byte being copied is of the value 0x20. By crafting a large enough string without this terminator, an attacker can exploit this to execute remote code under the context of the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
