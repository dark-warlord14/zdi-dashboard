# ZDI-18-1075: (0Day) Microsoft Windows Jet Database Engine Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1075
- **ZDI-CAN:** ZDI-CAN-6135
- **Date:** 2018-09-20
- **CVE:** CVE-2018-8423
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the management of indexes in the Jet database engine. Crafted data in a database file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8423 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/08/18 - ZDI reported the vulnerability to the vendor and the vendor acknowledged the report 05/14/18 - The vendor replied that they successfully reproduced the issue ZDI reported 09/09/18 - The vendor reported an issue with the fix and that the fix might not make the September release 09/10/18 - ZDI cautioned potential 0-day 09/11/18 - The vendor confirmed the fix did not make the build 09/12/18 - ZDI confirmed to the vendor the intention to 0-day on 09/20/18 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-09-20 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
