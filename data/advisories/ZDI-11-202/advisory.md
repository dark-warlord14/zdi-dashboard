# ZDI-11-202: Adobe Shockwave rcsL String Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-202
- **ZDI-CAN:** ZDI-CAN-1027
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2119
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-202/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing the rcsL RIFF chunk within Director files. The logic within the DIRAPI.dll module fails to account for a specific condition and can be made to misallocate a buffer on the heap. By crafting specific values within rcsL substructures an attacker can corrupt memory leading to arbitrary code execution under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
