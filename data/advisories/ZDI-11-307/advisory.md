# ZDI-11-307: Oracle Java MixerSequencer.nAddControllerEventCallback Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-307
- **ZDI-CAN:** ZDI-CAN-1218
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3545
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** axtaxt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-307/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists because Java does not sufficiently verify parameters certain functions. The function MixerSequencer.nAddControllerEventCallback fails to check for negative index numbers before writing user supplied data into a static array. This allows a malicious applet to write user controlled data outside the array boundaries resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2011-443431.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
