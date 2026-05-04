# ZDI-18-292: Microsoft Office Excel Slicer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-292
- **ZDI-CAN:** ZDI-CAN-5621
- **Date:** 2018-04-11
- **CVE:** CVE-2018-1011
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of slicers and timelines in Excel workbooks. A crafted filter in an Excel workbook can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-1011

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-04-11 - Coordinated public release of advisory
- 2018-04-11 - Advisory Updated
