# ZDI-11-207: Adobe Shockwave tSAC Chunk String Termination Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-207
- **ZDI-CAN:** ZDI-CAN-1080
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2118
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Donato Ferrante Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the support for embedding various file types within the RIFF-based Director file format. Several of the asset modules distributed with Shockwave do not properly extract string values from within embedded media objects. The code attempts to null-terminate such strings using a 32-bit size value specified prior to the string value. By crafting an embedded media object with a large string size an attacker can write a NULL byte to a controlled offset from the buffer containing the string. This can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
