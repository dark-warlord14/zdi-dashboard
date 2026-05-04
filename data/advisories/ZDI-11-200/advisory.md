# ZDI-11-200: Adobe Shockwave AudioMixer Structure Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-200
- **ZDI-CAN:** ZDI-CAN-1057
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2121
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within AudioMixer.x32 module responsible for parsing mixer structures from within Director movie files (.dir). While handling a size element, the code performs an unchecked multiplication operation which can cause an integer to wrap. This results in an undersized heap allocation which can be overflowed with user data leading to arbitrary code execution under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
