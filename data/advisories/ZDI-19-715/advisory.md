# ZDI-19-715: Microsoft Word DOC File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-715
- **ZDI-CAN:** ZDI-CAN-8599
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1201
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** L4Nce
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-715/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOC files. Crafted data in a DOC file can trigger an overflow of a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1201

## Disclosure Timeline

- 2019-05-29 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory
