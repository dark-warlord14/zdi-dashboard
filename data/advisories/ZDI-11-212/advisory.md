# ZDI-11-212: Adobe Shockwave KEY* Chunk Invalid Size Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-212
- **ZDI-CAN:** ZDI-CAN-1248
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2111
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Shockwave handles KEY* elements in a Director file. The Shockwave player will allocate memory with a size taken from the Shockwave file but will always copy a few bytes into that allocation. KEY* sizes smaller then 4 will therefore cause an overwrite of the allocation. By cleverly crafting the input file, an attacker can leverage this to execute remote code under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
