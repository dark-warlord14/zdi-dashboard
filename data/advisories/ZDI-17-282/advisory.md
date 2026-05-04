# ZDI-17-282: (Pwn2Own) Adobe Reader DC Collab documentToStream Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-282
- **ZDI-CAN:** ZDI-CAN-4589
- **Date:** 2017-08-01
- **CVE:** CVE-2017-3057
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** willj from Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-282/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Collab.documentToStream method. By manipulating a document's elements an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-03-19 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
