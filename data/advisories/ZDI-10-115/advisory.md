# ZDI-10-115: Adobe Flash Player AVM newFrameState Integer Overfow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-115
- **ZDI-CAN:** ZDI-CAN-511
- **Date:** 2010-06-25
- **CVE:** CVE-2010-2160
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AVM bytecode verifier. Specifically, the newFrameState method performs arithmetic when calculating the size of a stack frame. It implicitly trusts the max_scope and max_stack variables as obtained from the bytecode. By crafting specific values, the integer indicating the size of the frame can be made to overflow. This value is later used during memory copy operations which an attacker can influence to gain arbitrary code execution under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-14.html

## Disclosure Timeline

- 2009-06-26 - Vulnerability reported to vendor
- 2010-06-25 - Coordinated public release of advisory
