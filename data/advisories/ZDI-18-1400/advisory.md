# ZDI-18-1400: Adobe Reader DC Onix32 Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1400
- **ZDI-CAN:** ZDI-CAN-7311
- **Date:** 2018-12-12
- **CVE:** CVE-2018-19720
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1400/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of index files within Onix32.dll. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-09-27 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
