# ZDI-20-1253: Microsoft Excel XLS File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1253
- **ZDI-CAN:** ZDI-CAN-11529
- **Date:** 2020-10-19
- **CVE:** CVE-2020-16932
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16932

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
