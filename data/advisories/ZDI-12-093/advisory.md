# ZDI-12-093: (Pwn2Own) Microsoft Internet Explorer Fixed Table Colspan Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-093
- **ZDI-CAN:** ZDI-CAN-1547
- **Date:** 2012-06-12
- **CVE:** CVE-2012-1876
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** VUPEN Vulnerability Research Team http://www.vupen.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles dynamically changed colspans on a column in a table with the table-layout:fixed style. If the colspan is increased after initial creation it will result in a heap overflow. This can lead to remote code execution under the context of the current program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS12-037.mspx

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-06-12 - Coordinated public release of advisory
