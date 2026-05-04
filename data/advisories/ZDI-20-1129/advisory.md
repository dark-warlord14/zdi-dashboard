# ZDI-20-1129: Microsoft Windows Media Player HEVC Stream Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1129
- **ZDI-CAN:** ZDI-CAN-11215
- **Date:** 2020-09-10
- **CVE:** CVE-2020-1129
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HEVC streams. A crafted HEVC stream in a video file can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1129

## Disclosure Timeline

- 2020-06-04 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
