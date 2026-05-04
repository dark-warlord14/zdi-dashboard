# ZDI-21-1159: Microsoft Office Visio EMF File Parsing Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1159
- **ZDI-CAN:** ZDI-CAN-14216
- **Date:** 2021-10-14
- **CVE:** CVE-2021-40480
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1159/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40480

## Disclosure Timeline

- 2021-07-28 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
