# ZDI-16-645: Microsoft Windows Icon File Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-645
- **ZDI-CAN:** ZDI-CAN-4051
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7272
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Giwan Go of STEALIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-645/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file or folder. The specific flaw exists within the processing of icon files. The issue results from the lack of proper validation of user-supplied data which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms16-146

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
