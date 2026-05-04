# ZDI-17-929: Microsoft Office Excel XLS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-929
- **ZDI-CAN:** ZDI-CAN-5320
- **Date:** 2017-12-06
- **CVE:** CVE-2017-11884
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Dmitri Kaslov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-929/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2017-11884

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2017-12-06 - Coordinated public release of advisory
