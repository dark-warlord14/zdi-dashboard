# ZDI-20-992: Microsoft Windows WEBP VP8X Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-992
- **ZDI-CAN:** ZDI-CAN-10609
- **Date:** 2020-08-13
- **CVE:** CVE-2020-1574
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** @expend20
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-992/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of WEBP images. A crafted VP8X chunk can trigger an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1574

## Disclosure Timeline

- 2020-03-09 - Vulnerability reported to vendor
- 2020-08-13 - Coordinated public release of advisory
