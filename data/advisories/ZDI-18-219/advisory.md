# ZDI-18-219: Microsoft Office Excel XLS File Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-219
- **ZDI-CAN:** ZDI-CAN-5470
- **Date:** 2018-02-28
- **CVE:** CVE-2018-0841
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** A3F2160DCA1BDE70DA1D99ED267D5DC1EC336192
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-219/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XLS files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0841

## Disclosure Timeline

- 2017-12-07 - Vulnerability reported to vendor
- 2018-02-28 - Coordinated public release of advisory
- 2018-02-28 - Advisory Updated
