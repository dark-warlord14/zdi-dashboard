# ZDI-19-642: Microsoft Office Excel OLE Object Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-642
- **ZDI-CAN:** ZDI-CAN-7605
- **Date:** 2019-07-10
- **CVE:** CVE-2019-1111
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** yingxinlei
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-642/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Excel objects when invoked through OLE by other Office applications. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1111

## Disclosure Timeline

- 2019-01-25 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
