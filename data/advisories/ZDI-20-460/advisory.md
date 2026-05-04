# ZDI-20-460: Microsoft Windows JET Database Engine Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-460
- **ZDI-CAN:** ZDI-CAN-9968
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0992
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Bit, CodeBreaker, Meysam Firouzi, Jacob Soo Lead Re of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-460/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JET database engine. Crafted data in an MDB file can trigger an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0992

## Disclosure Timeline

- 2020-01-08 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
