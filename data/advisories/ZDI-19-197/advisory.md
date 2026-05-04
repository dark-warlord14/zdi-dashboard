# ZDI-19-197: Microsoft Access Database Engine ACEEXCL Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-197
- **ZDI-CAN:** ZDI-CAN-7405
- **Date:** 2019-02-12
- **CVE:** CVE-2019-0673
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Access Database Engine. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when reading and writing to XLS files. Crafted data in an XLS file can trigger a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0673

## Disclosure Timeline

- 2018-10-25 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
