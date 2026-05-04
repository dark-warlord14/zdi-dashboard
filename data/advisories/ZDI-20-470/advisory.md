# ZDI-20-470: Microsoft Excel XLS File Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-470
- **ZDI-CAN:** ZDI-CAN-10638
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0906
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** hackyzh and lm0963 of DBAppSecurity Zion Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-470/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XLS files. Crafted data in an XLS file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0906

## Disclosure Timeline

- 2020-03-05 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
