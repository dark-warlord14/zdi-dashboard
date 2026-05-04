# ZDI-20-251: Adobe FrameMaker TIF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-251
- **ZDI-CAN:** ZDI-CAN-9454
- **Date:** 2020-02-12
- **CVE:** CVE-2020-3740
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe FrameMaker. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of TIF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/framemaker/apsb20-04.html

## Disclosure Timeline

- 2019-12-03 - Vulnerability reported to vendor
- 2020-02-12 - Coordinated public release of advisory
