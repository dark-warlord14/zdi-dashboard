# ZDI-11-203: Adobe Shockwave xtcL Chunk Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-203
- **ZDI-CAN:** ZDI-CAN-1113
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2112
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-203/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing xtcL RIFF chunks within Director files. When attempting to allocate dynamic memory for substructures within this object, the code within DIRAPI.dll does not properly validate the size specified within the chunk. By crafting malicious values the process can be made to under-allocate a buffer which is later corrupted by memory copy operations. This can be leveraged by a remote attacker to execute code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
