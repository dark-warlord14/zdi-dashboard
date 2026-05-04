# ZDI-20-580: Adobe Bridge DCM File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-580
- **ZDI-CAN:** ZDI-CAN-10035
- **Date:** 2020-04-30
- **CVE:** CVE-2020-9568
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-580/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Bridge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of DCM files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb20-19.html

## Disclosure Timeline

- 2020-01-10 - Vulnerability reported to vendor
- 2020-04-30 - Coordinated public release of advisory
