# ZDI-17-249: Adobe Reader DC PRC Parsing Out-Of-Bound Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-249
- **ZDI-CAN:** ZDI-CAN-4212
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3019
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PRC streams. The process does not properly validate user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2016-11-30 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
