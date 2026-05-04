# ZDI-20-469: Microsoft Excel XLSM File Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-469
- **ZDI-CAN:** ZDI-CAN-10140
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0906
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** Zhihua Yao and Dexter Li
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-469/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of OLE streams in XLSM files. Crafted data in an XLSM file can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0906

## Disclosure Timeline

- 2020-02-10 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
