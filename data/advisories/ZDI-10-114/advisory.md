# ZDI-10-114: Adobe Flash Player AVM2 getouterscope Opcode Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-114
- **ZDI-CAN:** ZDI-CAN-511
- **Date:** 2010-06-25
- **CVE:** CVE-2010-2160
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Dionysus Blazakis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-114/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required in that a target must visit a malicious web page. The specific vulnerability exists within the parsing of an undocumented opcode within Adobe's ActionScript Virtual Machine 2 bytecode. The operand to this opcode is used as an offset to a structure and if set to a malicious value can be pointed to attacker controlled data. The structure contains a function pointer that is later called. If an attacker modifies the controlled data pointed to by the invalid offset, this function pointer can be set to point to malicious code thus gaining execution under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/go/apsb10-14

## Disclosure Timeline

- 2009-06-26 - Vulnerability reported to vendor
- 2010-06-25 - Coordinated public release of advisory
