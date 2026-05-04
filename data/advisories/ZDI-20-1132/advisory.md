# ZDI-20-1132: Microsoft Excel XLS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1132
- **ZDI-CAN:** ZDI-CAN-11276
- **Date:** 2020-09-10
- **CVE:** CVE-2020-1193
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** ecN4L
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. Crafted data in an XLS file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1193

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
