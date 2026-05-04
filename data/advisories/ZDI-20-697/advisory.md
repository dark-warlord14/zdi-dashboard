# ZDI-20-697: Microsoft Windows Media Player mpg2splt Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-697
- **ZDI-CAN:** ZDI-CAN-10681
- **Date:** 2020-06-09
- **CVE:** CVE-2020-1239
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-697/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the mpg2splt.ax module. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before reading from memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1239

## Disclosure Timeline

- 2020-03-05 - Vulnerability reported to vendor
- 2020-06-09 - Coordinated public release of advisory
