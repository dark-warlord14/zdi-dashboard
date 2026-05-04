# ZDI-20-1225: Trend Micro OfficeScan ServerMigrationTool ZIP File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1225
- **ZDI-CAN:** ZDI-CAN-11108
- **Date:** 2020-09-25
- **CVE:** CVE-2020-25774
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1225/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro OfficeScan ServerMigrationTool. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ZIP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000271974

## Disclosure Timeline

- 2020-05-29 - Vulnerability reported to vendor
- 2020-09-25 - Coordinated public release of advisory
