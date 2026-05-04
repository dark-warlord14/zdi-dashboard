# ZDI-10-070: Microsoft Windows Media Player Codec Retrieval Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-070
- **ZDI-CAN:** ZDI-CAN-619
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0268
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player 9
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. The specific flaw exists within the functionality for retrieving a codec for an unknown fourCC compression code. If an embedded Windows Media Player control attempts to play a media file containing an unknown codec it makes a request to Microsoft to retrieve the necessary capability. If the control is removed from the page while attempting to do this, cleanup routines will call an already freed pointer. An attacker can leverage this to execute arbitrary code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-027.mspx

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
