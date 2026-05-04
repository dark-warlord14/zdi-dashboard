# ZDI-19-448: (0Day) Microsoft Visual Studio asm Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-448
- **ZDI-CAN:** ZDI-CAN-7816
- **Date:** 2019-04-30
- **CVE:** N/A
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Simon Zuckerbraun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-448/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on executables compiled using vulnerable installations of Microsoft Visual Studio. Attack vectors will vary depending on the nature of the executable in question, but would include opening a specially crafted file which was compiled with an affected version of Visual Studio. The specific flaw exists within the compilation of __asm blocks in Visual C++. Incorrect output produced by the compiler can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 01/15/19 – ZDI sent the vulnerability report to the vendor 01/15/19 – The vendor replied with tracking number 01/24/19 – The vendor replied that they will not be pursuing a fix for this case due to stability issues in the 2015 version and the low severity rating based on attack vector 01/25/19 – ZDI asked the vendor to re-consider 01/25/19 – The vendor acknowledged the request 02/05/19 – ZDI requested any available update 02/08/19 - The vendor acknowledged the request 02/14/19 – ZDI requested any available update 02/21/19 – ZDI requested any available update 02/21/19 - The vendor acknowledged the request 04/02/19 – ZDI requested any available update 04/03/19 – The final reply back from the vendor was that they would not “port the change as hotfix from 15.9 to prior VS releases” -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-01-15 - Vulnerability reported to vendor
- 2019-04-30 - Coordinated public release of advisory
- 2019-11-01 - Advisory Updated
