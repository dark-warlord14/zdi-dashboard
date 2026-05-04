# ZDI-14-334: Sophos Cyberoam diagnose Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-334
- **ZDI-CAN:** ZDI-CAN-2332
- **Date:** 2014-10-01
- **CVE:** CVE-2014-5501
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sophos
- **Affected Products:** Cyberoam
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-334/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sophos Cyberoam. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the diagnose service. The issue lies in the failure to validate the size of the input buffer before copying it into a fixed-size buffer on the stack. An attacker can leverage this vulnerability to execute code under the context of the web server.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://kb.cyberoam.com/default.asp?id=3049&Lang=1&SID

## Disclosure Timeline

- 2014-06-04 - Vulnerability reported to vendor
- 2014-10-01 - Coordinated public release of advisory
