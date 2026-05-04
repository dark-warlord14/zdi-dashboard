# ZDI-10-162: Adobe Shockwave Director rcsL Chunk Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-162
- **ZDI-CAN:** ZDI-CAN-836
- **Date:** 2010-08-24
- **CVE:** CVE-2010-2873
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-162/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the rcsL RIFF chunk within director files of extension DIR or DCR. While parsing this undocumented structure, the application blindly trusts an offset value and uses it while operating on heap memory. An attacker can abuse this to corrupt a function pointer which can lead to arbitrary code execution under the context of the user running the web browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-20.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-08-24 - Coordinated public release of advisory
