# ZDI-10-067: Apple QuickTime Pict BkPixPat Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-067
- **ZDI-CAN:** ZDI-CAN-593
- **Date:** 2010-04-06
- **CVE:** CVE-2010-0529
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the primary QuickTime.qts library when parsing the BkPixPat opcode (0x12) within a PICT file. The application will use 2 fields within the file in a multiply which is then passed as an argument to an allocation. As both operands in the multiply are user-controllable, specific values can cause an under allocation which will later result in a heap overflow. Successful exploitation can lead to code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2009-11-06 - Vulnerability reported to vendor
- 2010-04-06 - Coordinated public release of advisory
