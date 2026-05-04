# ZDI-10-087: Adobe Shockwave Invalid Offset Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-087
- **ZDI-CAN:** ZDI-CAN-675
- **Date:** 2010-05-11
- **CVE:** CVE-2010-1281
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-087/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required in that a target visit a malicious website. The specific flaw exists within the code responsible for parsing Director files. The vulnerable function is exported as an ordinal from the iml32.dll module. Ordinal 1409 trusts a value from the file as an offset and updates pointers accordingly. By crafting a large enough value and seeking the file pointer past the end of a buffer this can be abused to corrupt heap memory. An attacker can abuse this to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-12.html

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-05-11 - Coordinated public release of advisory
