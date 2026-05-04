# ZDI-20-241: Adobe FrameMaker CEL File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-241
- **ZDI-CAN:** ZDI-CAN-9443
- **Date:** 2020-02-12
- **CVE:** CVE-2020-3731
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-241/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe FrameMaker. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CEL files. When parsing CEL files, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/framemaker/apsb20-04.html

## Disclosure Timeline

- 2019-10-31 - Vulnerability reported to vendor
- 2020-02-12 - Coordinated public release of advisory
