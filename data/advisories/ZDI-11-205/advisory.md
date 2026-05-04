# ZDI-11-205: Adobe Shockwave Missing Lctx Chunk Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-205
- **ZDI-CAN:** ZDI-CAN-1059
- **Date:** 2011-06-14
- **CVE:** CVE-2011-0335
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the RIFF-based Director file format that Shockwave utilizes. When parsing such files, the code within the dirapi.dll module expects to find a chunk with a fourCC value of Lctx. The code does not consider the possibility that one may not exist and in that scenario if fails to properly initialize certain values that are used later on in parsing other chunks. By removing the Lctx chunk and also filling heap memory, an attacker can take advantage of the uninitialized values to write values to an arbitrary location in memory. This can be leveraged to execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
